# -*- coding: utf-8 -*-

from django2_alexa.interfaces.response.alexa import AlexaResponse
from django2_alexa.interfaces.alexa import Skill
from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.interfaces.response.cards import SimpleCard


skill = Skill()


@skill.launch
def start_skill(request):
    speech = "starting card example for django2-alexa"
    card_text = "developed by Tim Woocker and Malte Mosler"
    return AlexaResponse(OutputSpeech(speech), SimpleCard(card_text))
    # displays other text than spoken.


@skill.intent("AMAZON.HelpIntent")
def help_intent(request):
    help_txt = "This skill is showing a card example."
    return AlexaResponse(OutputSpeech(help_txt), SimpleCard(help_txt))
    # displays the spoken text.
