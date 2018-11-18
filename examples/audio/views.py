# -*- coding: utf-8 -*-

from django2_alexa.interfaces.response import Response, audio_player
from django2_alexa.interfaces.response.cards import SimpleCard
from django2_alexa.interfaces.response.output_speech import OutputSpeech
from django2_alexa.interfaces.alexa import Skill
from random import randint
import os


skill = Skill()

SKILL_NAME = "music for children"
BASE_STREAM_URL = "https://www.skinssociety.com/alexa/kinder_musik_vocal/mp3/"


def random_song():
    song_list = []
    for root, dirs, files in os.walk("./static/music"):
        song_list = files
    return "{}".format(song_list[randint(0, (len(song_list) - 1))])
    # returns the name of a mp3 file


@skill.launch
def start_skill(request):
    speech = "starting {}".format(SKILL_NAME)
    song_name = random_song()
    display_text = "now playing: {}".format(song_name)
    stream_url = '{}/{}'.format(BASE_STREAM_URL, song_name)
    d = audio_player.Play(stream_url)
    return Response(OutputSpeech(speech), SimpleCard(display_text), directives=[d])


# @skill.on_playback_nearly_finished()
# def nearly_finished():
#    stream_url = '{}/{}'.format(sound_url, random_song())
#    return audio().enqueue(stream_url)


@skill.intent("AMAZON.HelpIntent")
def help_intent():
    help_txt = "This skill is playing {}. Say next to skip this song".format(SKILL_NAME)
    return Response(OutputSpeech(help_txt), should_end_session=False)


@skill.intent('AMAZON.PauseIntent')
def pause():
    pass


@skill.intent('AMAZON.ResumeIntent')
def resume():
    pass


@skill.intent('AMAZON.NextIntent')
def next_song():
    stream_url = '{}/{}'.format(BASE_STREAM_URL, random_song())
    pass


@skill.intent("AMAZON.CancelIntent")
def cancel_intent():
    return Response(OutputSpeech("You can't stop! Hahahaha"), should_end_session=True)


@skill.intent("AMAZON.StopIntent")
def stop_intent():
    return Response(OutputSpeech("You can't stop! Hahahaha"), should_end_session=True)


# @skill.session_ended
# def session_end():
#    return '{}', 200