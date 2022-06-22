import unittest
from bonsol.pricing_problem import pricing_problem


class TestPricingProblem(unittest.TestCase):
    def test_case0(self):
        val = pricing_problem(3600, 2.25, "MI")
        self.assertEqual(val, "$7984.98")

    def test_case1(self):
        val = pricing_problem(11100, 4.5, "QC")
        self.assertEqual(val, "$51687.01")

    def test_case2(self):
        val = pricing_problem(10, 1, "AB")
        self.assertEqual(val, "$10.5")

    def test_case3(self):
        val = pricing_problem(6050, 12.21, "AB")
        self.assertEqual(val, "$69807.62")

    def test_case4(self):
        val = pricing_problem(10000, 2.25, "DE")
        self.assertEqual(val, "$20250.0")

    def test_case5(self):
        val = pricing_problem(8000, 1, "QC")
        self.assertEqual(val, "$8554.14")

    def test_case6(self):
        val = pricing_problem(6000, 1, "QC")
        self.assertEqual(val, "$6553.58")


if __name__ == "__main__":
    unittest.main()
