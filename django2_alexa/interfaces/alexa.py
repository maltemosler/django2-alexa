from django.conf import settings
from django.http import HttpResponseServerError

from django2_alexa.interfaces.request.alexa import LaunchRequest
from django2_alexa.interfaces.request.base import BaseRequest
from django2_alexa.utils.s3_verification import is_valid_request


class Skill:
    _launch = None
    _intents = {}

    def view(self, request, *args, **kwargs):
        re = BaseRequest(request)
        if re.type == "LaunchRequest" and self._launch:
            return self._launch(request, *args, **kwargs)
        if re.type == "IntentRequest":
            name = re.body['intent']['name']
            if name in self._intents:
                return self._intents[name](request, *args, **kwargs)

    def launch(self, func):
        self._launch = func

        def wrapper(request, *args, **kwargs):
            if getattr(settings, "ALEXA_VERIFY_CONN", False) and not is_valid_request(request):
                # TODO: Troubleshooting part in docs
                return HttpResponseServerError("Amazon Server verification failed.")
            request.launch_request = LaunchRequest(request)
            return func(request, *args, **kwargs)
        return wrapper

    def intent(self, name: str):
        def inner(func):
            self._intents[name] = func

            def wrapper(request, *args, **kwargs):
                if getattr(settings, "ALEXA_VERIFY_CONN", False) and not is_valid_request(request):
                    return HttpResponseServerError("Amazon Server verification failed.")
                return func(request, *args, **kwargs)
            return wrapper
        return inner
