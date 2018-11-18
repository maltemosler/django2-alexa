from django.http import HttpRequest

from django2_alexa.interfaces.request.base import BaseRequest
from django2_alexa.interfaces.request.intent import Intent, ConfirmationStatus, Slot
from django2_alexa.utils.enums import DialogState
from django2_alexa.utils.enums.locales import Locale


class LaunchRequest(BaseRequest):
    def __init__(self, request: HttpRequest):
        super().__init__(request)
        self.request_id = self.body["requestId"]    # type: str
        self.timestamp = self.body["timestamp"]     # type: str
        self.locale = Locale(self.body["locale"])   # type: Locale


class IntentRequest(BaseRequest):
    def __init__(self, request: HttpRequest):
        super().__init__(request)
        self.request_id = self.body["requestId"]    # type: str
        self.timestamp = self.body["timestamp"]     # type: str
        self.locale = Locale(self.body["locale"])   # type: Locale
        self.dialog_state = DialogState(self.body["dialogState"])
        intent = self.body["intent"]
        slots = {}
        for s in intent["slots"]:
            for x in s["SlotName"]:
                slots[x.name] = Slot(x.name, x.value, x.confirmation_status)
        self.intent = Intent(intent["name"], ConfirmationStatus(intent["confirmationStatus"]))
