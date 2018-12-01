from django.http import HttpRequest

from django2_alexa.interfaces.request.base import BaseRequest


class WakeUpRequest(BaseRequest):
    def __init__(self, request: HttpRequest):
        super().__init__(request)
        self.namespace = self.body["namespace"]  # type: str
        self.name = self.body["name"]  # type: str
        self.payload_version = self.body["payloadVersion"]  # type: str
        self.message_id = self.body["messageId"]  # type: str
        self.correlation_token = self.body["correlationToken"]  # type: str
