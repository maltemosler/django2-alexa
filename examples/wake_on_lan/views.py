# -*- coding: utf-8 -*-

from django2_alexa.interfaces.response.alexa import AlexaResponse
from django2_alexa.interfaces.alexa import Skill
from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.interfaces.response import wake_on_lan


skill = Skill()


@skill.launch
def start_skill(request):
    mac_addresses = ["10-10-10-10-10-10"]
    speech = "okay bruder"
    return AlexaResponse(OutputSpeech(speech), directives=[wake_on_lan.WakeUp(mac_addresses)])
