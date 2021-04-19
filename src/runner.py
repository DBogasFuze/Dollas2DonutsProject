from logger import my_logger
from SpeechToText import my_speech_to_text

def main():
    my_logger.info("Starting automated Stenography...")
    my_speech_to_text.do_speech_recognition()


if __name__ == '__main__':
    main()







