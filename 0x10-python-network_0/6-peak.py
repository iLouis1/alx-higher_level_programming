#!/usr/bin/python3
"""This contains function find_peak"""


def find_peak(list_of_integers):
    """Will find a peak in a list of unsorted integers"""
    lx = list_of_integers
    l = len(lx)
    if l == 0:
        return
    m = l // 2
    if (m == l - 1 or lx[m] >= lx[m + 1]) and (m == 0 or lx[m] >= lx[m - 1]):
        return lx[m]
    if m != l - 1 and lx[m + 1] > lx[m]:
        return find_peak(lx[m + 1:])
    return find_peak(lx[:m])
