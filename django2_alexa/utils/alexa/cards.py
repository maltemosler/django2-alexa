from django.http import HttpRequest


class Card:
    def serialize(self):
        pass


class SimpleCard(Card):
    def __init__(self):
        self.type = "Simple"
        self.title = ""  # type: str
        self.content = ""  # type: str

    def serialize(self):
        d = {
            'type': self.type,
            'title': self.title,
            'content': self.content
        }
        return d


class StandardCard(Card):
    def __init__(self):
        self.type = "Standard"
        self.title = ""  # type: str
        self.text = ""  # type: str
        self.smallImageUrl = ""  # type: str
        self.largeImageUrl = ""  # type: str

    def serialize(self):
        d = {
            'type': self.type,
            'title': self.title,
            'text': self.text,
            'image': {
                'smallImageUrl': self.smallImageUrl,
                'largeImageUrl': self.largeImageUrl
            },
        }
        return d


class LinkAccountCard(Card):
    def __init__(self):
        self.type = "LinkAccount"

    def serialize(self):
        d = {
            'type': self.type
        }
        return d


class AskForPermissionsConsentCard(Card):
    def __init__(self):
        self.type = "AskForPermissionsConsent"
        self.title = ""  # type: str
        self.content = ""  # type: str
        self.text = ""  # type: str

    def serialize(self):
        d = {
            'type': self.type,
            'title': self.title,
            'content': self.content,
            'text': self.text
        }
        return d
