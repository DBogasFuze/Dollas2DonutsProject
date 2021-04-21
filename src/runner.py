from SpeechToText import my_speech_to_text
from logger import my_logger


def runner():
    my_logger.info("Starting automated Stenography...")
    my_speech_to_text.do_speech_recognition()


if __name__ == '__main__':
    runner()
