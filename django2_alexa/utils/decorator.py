from django.conf import settings
from django.http import HttpResponseServerError

from .s3_verification import is_valid_request


def intent(func):
    def wrapper(request, *args, **kwargs):
        if getattr(settings, "ALEXA_VERIFY_CONN", False) and not is_valid_request(request):
            # TODO: Troubleshooting part in docs
            return HttpResponseServerError("Amazon Server verification failed.")
        func(request, *args, **kwargs)
    return wrapper
