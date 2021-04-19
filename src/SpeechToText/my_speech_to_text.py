import speech_recognition as sr
from src.SpeechToText.my_session_manager import SessionManager
from src.logger import my_logger


def do_speech_recognition():
    session_manager = SessionManager("LaSession", "Session Person 1")
    recognizer = get_recognizer()
    text = ""
    session_stopper = "creative"
    while not session_stopper in text:
        audio = obtain_audio(recognizer)
        text = recognize_speech(recognizer, audio)
        session_manager.record_message_to_file(text)


def get_recognizer():
    return sr.Recognizer()


def get_microphone():
    return sr.Microphone()


def obtain_audio(recognizer):
    # obtain audio from the microphone
    with get_microphone() as source:
        my_logger.info("Say something!")
        audio = recognizer.listen(source)
    return audio


def recognize_speech(recognizer, audio):
    # recognize speech using Sphinx
    try:
        recognized_text = recognizer.recognize_sphinx(audio)
        my_logger.info("Sphinx thinks you said \"" + recognized_text + "\"")
        return recognized_text
    except sr.UnknownValueError:
        my_logger.info("Sphinx could not understand audio")
    except sr.RequestError as e:
        my_logger.info("Sphinx error; {0}".format(e))
