import os

def create_dir(directory):
    if not os.path.exists(directory):
        print("Creating directory...")
        os.makedirs(directory)


def write_file(path, data):
    f = open(path, 'w')
    print("Writing in to the file = ", f.name)
    f.write(data)
    f.close()
