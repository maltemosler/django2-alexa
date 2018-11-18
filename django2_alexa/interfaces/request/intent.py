from enum import Enum
from django2_alexa.interfaces.request.base import BaseRequest
from django.http import HttpRequest
from django2_alexa.utils.enums.locales import Locale


class ConfirmationStatus(Enum):
    NONE = "NONE"
    CONFIRMED = "CONFIRMED"
    DENIED = "DENIED"


class Resolution:
    def __init__(self):
        self.resolutionsPerAuthority = []


class Slot:
    def __init__(self, name: str, value: str, confirmation_status: ConfirmationStatus, resolutions: str=None):
        self.name = name
        self.value = value
        self.confirmation_status = ConfirmationStatus(confirmation_status)
        self.resolutions = Resolution()

    def to_dict(self):
        d = {
            'name': self.name,
            'value': self.value,
            'confirmationStatus': self.confirmation_status,
        }
        if self.resolutions:
            d['resolutions'] = self.resolutions
        return d


class Intent:
    def __init__(self, name: str, confirmation_status: ConfirmationStatus, slot: Slot):
        self.name = name
        self.confirmation_status = confirmation_status
        self.slots = slot

    def to_dict(self):
        d = {
            'name': self.name,
            'confirmationStatus': self.confirmation_status,
            'slots': self.slots
        }
        return d

