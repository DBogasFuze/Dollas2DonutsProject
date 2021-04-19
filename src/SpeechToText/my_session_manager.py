from src.atomic_ticker.my_atomic_clock import get_atomic_timestamp
from src.logger import my_logger
import os
from os import sep as separator


def create_message(message, person_name):
    my_logger.debug("Creating message to record in file")
    msg_time = get_atomic_timestamp()
    timestamp = msg_time.strftime("[%Y-%m-%d %H:%M:%S]")
    formatted_msg = timestamp + "[" + person_name + "]" + message + "\n"
    return formatted_msg


def create_folder(folder_name):
    my_logger.info("Creating a folder for session \" " + folder_name + "\"")
    parent_dir = os.getcwd() + separator + "results" + separator
    path = os.path.join(parent_dir, folder_name)
    my_logger.info("folder @ "+path)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(path, filename):
    my_logger.info("Creating a file for this session")
    abs_path = os.path.join(path, filename)
    f = open(abs_path, "w+")
    my_logger.info("name is " + f.name)
    return f.name


def append_to_file(filename, message, person_name):
    my_logger.info("appending message to file")
    f = open(filename, "a+")
    f.write(create_message(message, person_name))


class SessionManager:

    session_name = ""
    person_name = ""
    file_name = ""

    def __init__(self, session_name, person_name):
        self.session_name = session_name
        self.person_name = person_name
        self.file_name = self.start_session()

    def start_session(self):
        my_logger.info("Starting Session...")
        path = create_folder(self.session_name)
        file_path = create_file(path, self.session_name + ".txt")
        return file_path

    def record_message_to_file(self, message):
        my_logger.info("Recording message to file")
        append_to_file(self.file_name, message, self.person_name)
