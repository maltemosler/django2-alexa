from django.http import HttpRequest


class SimpleCard:
    def __init__(self, request: HttpRequest):
        self.type = "Simple"
        self.title = ""         # type: str
        self.content = ""       # type: str


class StandardCard:
    def __init__(self, request: HttpRequest):
        self.type = "Standard"
        self.title = ""             # type: str
        self.text = ""              # type: str
        self.image = object         # type:
        self.smallImageUrl = ""     # type: str
        self.largeImageUrl = ""     # type: str


class LinkAccountCard:
    def __init__(self, request: HttpRequest):
        self.type = "LinkAccount"


class AskForPermissionsConsentCard:
    def __init__(self, request: HttpRequest):
        self.type = "AskForPermissionsConsent"
        self.title = ""         # type: str
        self.content = ""       # type: str
        self.text = ""          # type: str
