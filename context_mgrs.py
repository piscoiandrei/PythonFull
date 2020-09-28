from contextlib import contextmanager


class ManagedFile:  # custom context manager # no library needed for this
    def __init__(self, filename):
        print("init")
        self.filename = filename

    def __enter__(self):
        print("enter")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        # after you handled the exeption return True so that the 'with'
        # statement won't raise the exception
        if exc_type is not None:
            print("Exeption has been handled")

        print("exit")
        return True


"""
from context_mgrs import *

with ManagedFile("text.txt") as my_file:
    print("do somethingggg")
    my_file.write("some textfgergerger")
"""


# CONTEXT MANAGER USING FUNCTION

def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()


with open_managed_file("notes.txt") as fl:
    fl.write("something to do.....")
