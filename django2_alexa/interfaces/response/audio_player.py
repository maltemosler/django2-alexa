import uuid

from django2_alexa.utils import Directive
from django2_alexa.utils.enums.play_behavior import PlayBehavior


class AudioMeta:
    def __init__(self, title: str = None, subtitle: str = None):
        # TODO: art & background image (Part of the display interface)
        self.title = title
        self.subtitle = subtitle

    def to_dict(self):
        d = {}
        if self.title:
            d['title'] = self.title
        if self.subtitle:
            d['subtitle'] = self.subtitle
        return d


class Play(Directive):
    def __init__(self, url: str, play_behavior=PlayBehavior.REPLACE_ALL, offset=0, previous_token: str = None,
                 meta: AudioMeta = None):
        self.play_behavior = play_behavior
        self.url = url
        self.token = str(uuid.uuid4())
        self.previous_token = previous_token or str(uuid.uuid4())
        self.offset = offset
        self.meta = meta

    def to_dict(self):
        d = {
            'type': "AudioPlayer.Play",
            'playBehavior': self.play_behavior.value,
            'audioItem': {
                'stream': {
                    'url': self.url,
                    'token': self.token,
                    'expectedPreviousToken': self.previous_token,
                    'offsetInMilliseconds': self.offset
                }
            }
        }
        if self.meta:
            d["audioItem"]["metadata"] = self.meta.to_dict()
        return d
