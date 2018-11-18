from enum import Enum


class ConfirmationStatus(Enum):
    NONE = "NONE"
    CONFIRMED = "CONFIRMED"
    DENIED = "DENIED"


class Slot:
    def __init__(self, name: str, value: str, confirmation_status: ConfirmationStatus):
        self.name = name
        self.value = value
        self.confirmation_status = ConfirmationStatus(confirmation_status)
        # TODO: Resolutions

    def to_dict(self):
        d = {
            'name': self.name,
            'value': self.value,
            'confirmationStatus': self.confirmation_status,
        }
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
