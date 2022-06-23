def solution(A):
    length = len(A)
    A = sorted(A)
    if A is None or length == 0:
        return 1
    if A[len(A) - 1] <= 0:
        return 1
    checker = False
    for i in range(0, len(A)):
        if A[i] == 1:
            checker = True
    if checker == False:
        return 1
    for i in range(0, len(A) - 1):
        if A[i] > 0 and (A[i + 1] - A[i]) > 1:
            return A[i] + 1
    return A[len(A) - 1] + 1