import unittest
from bonsol.odd_occ import solution


class TestOddOcc(unittest.TestCase):
    def test_case0(self):
        testcase = [9, 3, 9, 3, 9, 7, 9]
        val = solution(testcase)
        self.assertEqual(val, 7)

    def test_case1(self):
        testcase = [0]
        val = solution(testcase)
        self.assertEqual(val, 0)

    def test_case2(self):
        testcase = []
        val = solution(testcase)
        self.assertEqual(val, 0)

    def test_case3(self):
        testcase = [2, 4, 6, 8, 2, 9, 4, 6, 8]
        val = solution(testcase)
        self.assertEqual(val, 9)

    def test_case4(self):
        testcase = [1000000, 3, 3, 8, 9, 2, 9, 8, 1000000]
        val = solution(testcase)
        self.assertEqual(val, 2)

    def test_case5(self):
        testcase = [1,1,2,2,3,3,4,4,1]
        val = solution(testcase)
        self.assertEqual(val, 1)


if __name__ == "__main__":
    unittest.main()
