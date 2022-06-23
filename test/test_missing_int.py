import unittest
from bonsol.missing_int import solution


class TestMissingInt(unittest.TestCase):
    def test_case0(self):
        testcase = [1, 3, 6, 4, 1, 2]
        val = solution(testcase)
        self.assertEqual(val, 5)

    def test_case1(self):
        testcase = [0]
        val = solution(testcase)
        self.assertEqual(val, 1)

    def test_case2(self):
        testcase = []
        val = solution(testcase)
        self.assertEqual(val, 1)

    def test_case3(self):
        testcase = [1, 2, 3]
        val = solution(testcase)
        self.assertEqual(val, 4)

    def test_case4(self):
        testcase = [-1, -3]
        val = solution(testcase)
        self.assertEqual(val, 1)

    def test_case5(self):
        testcase = [-1, -2, 2, 4, 6]
        val = solution(testcase)
        self.assertEqual(val, 1)

    def test_case6(self):
        testcase = [-1000000,0,1000000]
        val = solution(testcase)
        self.assertEqual(val, 1)

    def test_case7(self):
        testcase = [1,2,3,4,6,7,8,10,11]
        val = solution(testcase)
        self.assertEqual(val, 5)

    def test_case8(self):
        testcase = [1]
        val = solution(testcase)
        self.assertEqual(val, 2)


if __name__ == "__main__":
    unittest.main()
