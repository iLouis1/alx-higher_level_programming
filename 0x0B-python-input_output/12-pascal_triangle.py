#!/usr/bin/python3
"""This defines Pascal's Triangle function."""


def pascal_triangle(n):
    """This representr Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """

    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]

        for g in range(len(tri) - 1):
            tmp.append(tri[g] + tri[g + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
