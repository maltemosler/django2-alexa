import json

from django.http import HttpRequest


class BaseRequest:
    def __init__(self, request: HttpRequest):
        data = json.loads(request.body.decode())
        self.body = data['request']   # type: dict
        self.type = self.body['type']
        self.user_id = data["context"]["System"]["user"]["userId"]
