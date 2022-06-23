def solution(S):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    if (len(S) == 1):
        return 0
    for i in S:
        # first bracket correct, storing into list
        if i in pairs.keys():
            stack.append(i)
        # check if most recent right bracket matches left bracket
        elif stack and i == pairs[stack[-1]]:
            stack.pop()
        else:
            return 0
    return 1
