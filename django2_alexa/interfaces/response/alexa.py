import json

from django.http import HttpResponse

from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.utils.alexa.cards import Card


class Response(HttpResponse):
    def __init__(self, output_speech: OutputSpeech = None, card: Card = None, reprompt: OutputSpeech = None,
                 should_end_session=True, directives: [object] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.output_speech = output_speech
        self.card = card
        self.reprompt = reprompt
        self.should_session_end = should_end_session
        # TODO: directives

        self["Content-Type"] = "application/json;charset=UTF-8"

    def serialize(self):
        d = {
            'version': "1.0",
            # TODO: 'sessionAttributes': None,
            'response': {
                'shouldEndSession': self.should_session_end,
                # TODO: directives
            }
        }
        if self.output_speech:
            d['response']['outputSpeech'] = self.output_speech.to_dict()
        if self.card:
            d['response']['card'] = self.card.to_dict()
        if self.reprompt:
            d['response']['reprompt'] = self.reprompt.to_dict()
        # return self.serialize_headers() + b'\r\n\r\n' + json.dumps(d).encode()
        return json.dumps(d).encode()
