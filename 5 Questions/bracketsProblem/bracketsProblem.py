import unittest

def solution(S):
    pairs = {"{": "}", "(": ")", "[": "]"}
    stack = []
    for i in S:
        # first bracket correct, storing into list
        if i in "{[(": 
            stack.append(i)
        #check if most recent right bracket matches left bracket
        elif stack and i == pairs[stack[-1]]:
            stack.pop()
        else:
            return 0
    return 1



class testBracketsProblem(unittest.TestCase):

    def test_case0(self):
        list=[]
        val = solution(list)
        self.assertEqual(val, 1)
    
    def test_case1(self):
        list=[")"]
        val = solution(list)
        self.assertEqual(val, 0)
    
    def test_case2(self):
        list=["[[]}])"]
        val = solution(list)
        self.assertEqual(val, 0)

    def test_case3(self):
        list=["{[()()]}"]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case4(self):
        list=["{[(])}"]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case5(self):
        list=["{{[[(())]]}}"]
        val = solution(list)
        self.assertEqual(val, 1)
        
    def test_case5(self):
        list=["([)()]"]
        val = solution(list)
        self.assertEqual(val, 0)

if __name__=='__main__':
    unittest.main()