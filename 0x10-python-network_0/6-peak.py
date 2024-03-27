#!/usr/bin/python3
"""This finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Will find a peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    lo = 0
    ki = len(list_of_integers)
    mid = ((ki - lo) // 2) + lo
    mid = int(mid)

    if ki == 1:
        return list_of_integers[0]

    if ki == 2:
        return max(list_of_integers)

    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])

    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
