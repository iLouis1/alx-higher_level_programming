#!/usr/bin/python3
"""This defines text file-reading functions."""


def read_file(filename=""):
    """Print the contents of UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
