import unittest
from bonsol.min_avg_two_slice import solution


class TestMinAvgTwoSlice(unittest.TestCase):
    def test_case0(self):
        testcase = [4, 2, 2, 5, 1, 5, 8]
        val = solution(testcase)
        self.assertEqual(val, 1)

    def test_case1(self):
        testcase = [4, 5, 6, 4, 8, 1, 1]
        val = solution(testcase)
        self.assertEqual(val, 5)

    def test_case2(self):
        testcase = [1, 1, 6, 4, 8, 1, 1]
        val = solution(testcase)
        self.assertEqual(val, 0)

    def test_case3(self):
        testcase = [1, 1, 6, 4, 8, 1, 1]
        val = solution(testcase)
        self.assertEqual(val, 0)

if __name__ == "__main__":
    unittest.main()
