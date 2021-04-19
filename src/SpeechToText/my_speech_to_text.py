#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr


def do_speech_recognition():
    recognizer = get_recognizer()
    audio = obtain_audio(recognizer)
    recognize_speech(recognizer,audio)


def get_recognizer():
    return sr.Recognizer()


def get_microphone():
    return sr.Microphone()


def obtain_audio(recognizer):

    # obtain audio from the microphone
    with get_microphone() as source:
        print("Say something!")
        audio = recognizer.listen(source)
    return audio


def recognize_speech(recognizer, audio):

    # recognize speech using Sphinx
    try:
        print("Sphinx thinks you said \"" + recognizer.recognize_sphinx(audio)+"\"")
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))
