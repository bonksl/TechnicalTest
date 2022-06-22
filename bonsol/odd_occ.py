import unittest


def solution(A):
    length = len(A)
    if A is None or length == 0:
        return 0
    if length == 1:
        return A[0]
    A = sorted(A)
    A.append(-1)
    for i in range(0, length, 2):
        if A[i] != A[i + 1]:
            return A[i]
