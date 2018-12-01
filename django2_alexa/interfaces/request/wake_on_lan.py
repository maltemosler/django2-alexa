import json

from django.http import HttpRequest


class WakeUpRequest:
    def __init__(self, request: HttpRequest):
        super().__init__(request)

        self._data = json.loads(request.body.decode())
        self.body = self._data['request']   # type: dict
        self.type = self.body['type']
        self.user_id = self._data["context"]["System"]["user"]["userId"]

        self.namespace = self.body["namespace"]  # type: str
        self.name = self.body["name"]  # type: str
        self.payload_version = self.body["payloadVersion"]  # type: str
        self.message_id = self.body["messageId"]  # type: str
        self.correlation_token = self.body["correlationToken"]  # type: str
