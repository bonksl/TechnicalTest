import unittest
from bonsol.missing_int import solution


class TestMissingInt(unittest.TestCase):
    def test_case0(self):
        list = [1, 3, 6, 4, 1, 2]
        val = solution(list)
        self.assertEqual(val, 5)

    def test_case1(self):
        list = [0]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case2(self):
        list = []
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case3(self):
        list = [1, 2, 3]
        val = solution(list)
        self.assertEqual(val, 4)

    def test_case4(self):
        list = [-1, -3]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case5(self):
        list = [-1, -2, 2, 4, 6]
        val = solution(list)
        self.assertEqual(val, 1)


if __name__ == "__main__":
    unittest.main()
