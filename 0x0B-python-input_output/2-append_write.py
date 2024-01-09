#!/usr/bin/python3
"""This defines a file-appending function."""


def append_write(filename="", text=""):

    """Appends a string to end of a UTF8 text file.

    Args:
        filename (str): This is the name of file to append to.
        text (str): This is the string to append to the file.

    Returns:
        The number of characters appended.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
