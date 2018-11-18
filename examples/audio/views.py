# -*- coding: utf-8 -*-
from django2_alexa.interfaces.response import audio_player
from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.interfaces.alexa import Skill
from django2_alexa.interfaces.response.alexa import AlexaResponse
from random import randint


skill = Skill()
user_offsets = {}
user_songs = {}


def random_song():
    song_list = [
        "Old_MacDonald.mp3",
        "London_Bridge_vocal.mp3",
        "This_Old_Man_vocal.mp3"
    ]
    return "{}".format(song_list[randint(0, (len(song_list) - 1))])
    # returns random song


@skill.launch
def start_skill(request):
    speech = "starting music for children"
    song = random_song()
    stream_url = "https://www.skinssociety.com/alexa/kinder_musik_vocal/mp3/{}".format(song)
    user_songs[request.user_id] = song
    return AlexaResponse(OutputSpeech(speech), directives=[audio_player.Play(stream_url)])


@skill.intent("AMAZON.HelpIntent")
def help_intent(request):
    help_txt = "This skill is playing music."
    return AlexaResponse(OutputSpeech(help_txt))


@skill.intent('AMAZON.PauseIntent')
def pause(request):
    return AlexaResponse(directives=[audio_player.Stop()])


@skill.playback_stopped
def pause(request):
    user_offsets[request.user_id] = request.offset
    return AlexaResponse()


@skill.intent('AMAZON.ResumeIntent')
def resume(request):
    song = user_songs[request.user_id]
    stream_url = "https://www.skinssociety.com/alexa/kinder_musik_vocal/mp3/{}".format(song)
    return AlexaResponse(directives=[audio_player.Play(stream_url, offset=user_offsets[request.user_id])])


@skill.intent('AMAZON.NextIntent')
def next_track(request):
    song = random_song()
    stream_url = "https://www.skinssociety.com/alexa/kinder_musik_vocal/mp3/{}".format(song)
    user_songs[request.user_id] = song
    return AlexaResponse(directives=[audio_player.Play(stream_url)])


@skill.intent("AMAZON.CancelIntent")
def cancel_intent(request):
    return AlexaResponse(directives=[audio_player.Stop()])


@skill.intent("AMAZON.StopIntent")
def stop_intent(request):
    return AlexaResponse(directives=[audio_player.Stop()])


# @skill.session_ended
# def session_end(request):
#    return '{}', 200
