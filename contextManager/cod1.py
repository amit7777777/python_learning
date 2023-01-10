# Python program showing
# file management using
# context manager

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        print("here in  class")
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print("here in  enter...")
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()


# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)
