#!/usr/bin/python3
"""This defines Python class-to-JSON function."""


def class_to_json(obj):

    """This returns dictionary represntation of a simple data structure."""

    return obj.__dict__
