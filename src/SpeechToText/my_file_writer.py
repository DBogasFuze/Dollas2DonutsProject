
def create_file(filename):
    f = open(filename + ".txt", "w+")
    print("name is "+ f.name)
    return f.name


def append_to_file(filename, message):
    f = open(filename + ".txt", "a+")
    f.write(message)
