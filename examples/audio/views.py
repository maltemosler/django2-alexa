# -*- coding: utf-8 -*-

from django2_alexa.interfaces.response import AlexaResponse, audio_player
from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.interfaces.alexa import Skill

skill = Skill()


@skill.launch
def start_skill(request):
    speech = "starting music for children"
    stream_url = "https://www.skinssociety.com/alexa/kinder_musik_vocal/mp3/Old_MacDonald.mp3"
    d = audio_player.Play(stream_url)
    return AlexaResponse(OutputSpeech(speech), directives=[d])


@skill.intent("AMAZON.HelpIntent")
def help_intent():
    help_txt = "This skill is playing music."
    return AlexaResponse(OutputSpeech(help_txt), should_end_session=False)


@skill.intent('AMAZON.PauseIntent')
def pause():
    pass


@skill.intent('AMAZON.ResumeIntent')
def resume():
    pass


@skill.intent("AMAZON.CancelIntent")
def cancel_intent():
    return AlexaResponse(OutputSpeech("You can't stop! Hahahaha"), should_end_session=True)


@skill.intent("AMAZON.StopIntent")
def stop_intent():
    return AlexaResponse(OutputSpeech("You can't stop! Hahahaha"), should_end_session=True)


# @skill.session_ended
# def session_end():
#    return '{}', 200
