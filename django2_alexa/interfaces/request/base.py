import json

from django.http import HttpRequest


class BaseRequest:
    def __init__(self, request: HttpRequest):
        data = json.loads(request.body.decode())
        self.user_id = data["session"]["user"]["userId"]
        self.session_id = data["session"]["sessionId"]
        self.body = data['request']   # type: dict
        self.type = self.body['type']
