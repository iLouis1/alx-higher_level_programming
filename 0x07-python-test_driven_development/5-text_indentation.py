#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to be printed.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    y = 0
    while y < len(text) and text[y] == ' ':
        y += 1

    while y < len(text):
        print(text[y], end="")
        if text[y] == "\n" or text[y] in ".?:":
            if text[y] in ".?:":
                print("\n")
            y += 1
            while y < len(text) and text[y] == ' ':
                y += 1
            continue
        y += 1
