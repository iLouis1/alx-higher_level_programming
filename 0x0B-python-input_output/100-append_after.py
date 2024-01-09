#!/usr/bin/python3
"""This defines text file insertion function."""


def append_after(filename="", search_string="", new_string=""):

    """Will insert text after each line containing a given string in a file.
    Args:
        filename (str): This is the name of the file.
        search_string (str): String to search for within the file.
        new_string (str): The string to be inserted.
    """

    text = ""
    with open(filename) as k:
        for line in k:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
