import unittest
from bonsol.brackets_problem import solution

class TestBracketsProblem(unittest.TestCase):
    def test_case0(self):
        inputstring = ""
        val = solution(inputstring)
        self.assertEqual(val, 1)

    def test_case1(self):
        inputstring = ")"
        val = solution(inputstring)
        self.assertEqual(val, 0)

    def test_case2(self):
        inputstring = "[[]}])"
        val = solution(inputstring)
        self.assertEqual(val, 0)

    def test_case3(self):
        inputstring = "{[()()]}"
        val = solution(inputstring)
        self.assertEqual(val, 1)

    def test_case4(self):
        inputstring = "{[(])}"
        val = solution(inputstring)
        self.assertEqual(val, 0)

    def test_case5(self):
        inputstring = "{{[[(())]]}}"
        val = solution(inputstring)
        self.assertEqual(val, 1)

    def test_case6(self):
        inputstring = "([)()]"
        val = solution(inputstring)
        self.assertEqual(val, 0)
    
    def test_case7(self):
        inputstring = "("
        val = solution(inputstring)
        self.assertEqual(val, 0)
    

if __name__ == "__main__":
    unittest.main()
