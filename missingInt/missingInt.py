import unittest


def solution(A):
    length = len(A)
    A=sorted(A)
    if A is None or length ==0:
        return 1
    if A[len(A)-1]<=0:
        return 1
    checker=False
    for i in range(0, len(A)):
        if A[i]==1:
            checker = True
    if checker ==False:
        return 1
    for i in range(0, len(A)-1):
        if A[i]>0 and (A[i+1]-A[i])>1:
            return A[i]+1
    return A[len(A)-1]+1


class testPricingProblem(unittest.TestCase):

    def test_case0(self):
        list=[1,3,6,4,1,2]
        val = solution(list)
        self.assertEqual(val, 5)

    def test_case1(self):
        list=[0]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case2(self):
        list=[]
        val = solution(list)
        self.assertEqual(val, 1)

    def test_case3(self):
        list=[1,2,3]
        val = solution(list)
        self.assertEqual(val, 4)

    def test_case4(self):
        list=[-1,-3]
        val = solution(list)
        self.assertEqual(val, 1)
    
    def test_case5(self):
        list=[-1,-2,2,4,6]
        val = solution(list)
        self.assertEqual(val, 1)



if __name__=='__main__':
    unittest.main()