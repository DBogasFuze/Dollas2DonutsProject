from src.atomic_ticker.my_atomic_clock import get_atomic_timestamp
from src.logger import my_logger
import os


def start_session(session_name):
    path = create_folder(session_name)
    create_file(path, session_name + ".txt")


def create_folder(folder_name):
    my_logger.info("Creating a folder for session \" " + folder_name + "\"")
    parent_dir = os.getcwd() + "/results/"
    path = os.path.join(parent_dir, folder_name)
    my_logger.info("folder @ "+path)
    os.mkdir(path)
    return path


def create_file(path, filename):
    abs_path = os.path.join(path, filename)
    f = open(abs_path, "w+")
    print("name is " + f.name)
    return f.name


def append_to_file(filename, message):
    f = open(filename + ".txt", "a+")
    f.write(message)


def create_message(message):
    msg_time = get_atomic_timestamp()
    timestamp = msg_time.strftime("%Y-%m-%d %H:%M:%S")
    my_logger.info(timestamp + " " + message)
