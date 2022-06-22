import unittest


def solution(A):
    minVal = 10000
    minIdx = 0
    for i in range(0, len(A) - 2):
        # calculate the three point average
        avg1 = (A[i] + A[i + 1] + A[i + 2]) / 3
        # calculate the two point average
        avg2 = (A[i] + A[i + 1]) / 2
        # check if avgs are lower than our previous minimum avg and get the index of it
        if minVal > avg1 or minVal > avg2:
            minVal = min(avg1, avg2)
            minIdx = i
    # check if its the last two index
    if minVal > (A[-1] + A[-2]) / 2:
        return len(A) - 2
    return minIdx
