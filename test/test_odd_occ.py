import unittest
from bonsol.odd_occ import solution


class TestOddOcc(unittest.TestCase):
    def test_case0(self):
        list = [9, 3, 9, 3, 9, 7, 9]
        val = solution(list)
        self.assertEqual(val, 7)

    def test_case1(self):
        list = [0]
        val = solution(list)
        self.assertEqual(val, 0)

    def test_case2(self):
        list = []
        val = solution(list)
        self.assertEqual(val, 0)

    def test_case3(self):
        list = [2, 4, 6, 8, 2, 9, 4, 6, 8]
        val = solution(list)
        self.assertEqual(val, 9)

    def test_case4(self):
        list = [1000000, 3, 3, 8, 9, 2, 9, 8, 1000000]
        val = solution(list)
        self.assertEqual(val, 2)


if __name__ == "__main__":
    unittest.main()
