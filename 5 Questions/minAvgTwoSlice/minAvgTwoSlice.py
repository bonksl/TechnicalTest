import unittest

def solution(A):
    minVal = 10000 
    minIdx = 0
    for i in range(0, len(A)-2):
        avg1 = (A[i] + A[i+1] + A[i+2]) / 3
        avg2 = (A[i] + A[i+1]) / 2
        if minVal > avg1 or minVal > avg2:
            minVal = min(avg1,avg2)
            minIdx=i

    if minVal > (A[-1] + A[-2]) / 2:
        return len(A)-2
    return minIdx

class testPricingProblem(unittest.TestCase):

    def test_case0(self):
        list=[4,2,2,5,1,5,8]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case1(self):
        list=[4,5,6,4,8,1,1]
        val = solution(list)
        self.assertEqual(val, 5)

    def test_case2(self):
        list=[1,1,6,4,8,1,1]
        val = solution(list)
        self.assertEqual(val, 0)
        
if __name__=='__main__':
    unittest.main()