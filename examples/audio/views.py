# -*- coding: utf-8 -*-

from django2_alexa.interfaces.response import Response, audio_player
from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.interfaces.alexa import Skill

skill = Skill()


@skill.launch
def start_skill(request):
    speech = "starting music for children"
    stream_url = "https://www.skinssociety.com/alexa/kinder_musik_vocal/mp3/Old_MacDonald.mp3"
    d = audio_player.Play(stream_url)
    return Response(OutputSpeech(speech), directives=[d])


@skill.intent("AMAZON.HelpIntent")
def help_intent(request):
    help_txt = "This skill is playing music."
    return Response(OutputSpeech(help_txt), should_end_session=False)


@skill.intent('AMAZON.PauseIntent')
def pause(request):
    pass


@skill.intent('AMAZON.ResumeIntent')
def resume(request):
    pass


@skill.intent("AMAZON.CancelIntent")
def cancel_intent(request):
    return Response(OutputSpeech("You can't stop! Hahahaha"), should_end_session=True)


@skill.intent("AMAZON.StopIntent")
def stop_intent(request):
    return Response(OutputSpeech("You can't stop! Hahahaha"), should_end_session=True)


# @skill.session_ended
# def session_end(request):
#    return '{}', 200
