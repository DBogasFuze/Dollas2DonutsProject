from logger import my_logger
from SpeechToText import my_speech_to_text
from SpeechToText import my_file_writer


def main():
    my_logger.info("Starting automated Stenography...")
    #my_speech_to_text.do_speech_recognition()
    my_file_writer.start_session("session2")


if __name__ == '__main__':
    main()







