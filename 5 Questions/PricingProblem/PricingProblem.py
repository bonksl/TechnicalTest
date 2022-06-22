import sys
import unittest


def pricingProblem(item, price, prov):
    discount=[1000,5000,7000,10000]
    province = ["AB","ON","QC","MI","DE"]
    total=0
    total=item*price
    for discounts in discount:
        #3% discount rate
        if 1000<=total and total<5000:
            total=total-total*0.03
            break
        #5% discount rate
        elif 5000<=total and total<7000:
            total=total-total*0.05
            break
        #7% discount rate
        elif 7000<=total and total<10000:
            total=total-total*0.07
            break
        #10% discount rate
        elif 10000<=total:
            total=total-total*0.1
            break
        #no discount rate
        else:
            break

    for provinces in province:
        #5% tax
        if prov=="AB":
            total=total*1.05
            break
        #13% tax
        elif prov=="ON":
            total=total*1.13
            break
        #14.975% tax
        elif prov=="QC":
            total=total*1.14975
            break
        #6% tax
        elif prov=="MI":
            total=total*1.06
            break
        #no tax
        elif prov=="DE":
            break
        else:
            break
    return ("$"+str(round(total,2)))

    #print(str(item)+" items, "+ str(price)+" per item, " +prov)
    #print("$"+str(round(total,2)))
    #print(str(items)+" items, "+ str(price)+" per item, " +prov)

class testPricingProblem(unittest.TestCase):

    def test_case0(self):
        val = pricingProblem(3600,2.25,"MI")
        self.assertEqual(val, "$7984.98")

    def test_case1(self):
        val = pricingProblem(11100,4.5,"QC")
        self.assertEqual(val, "$51687.01")

    def test_case2(self):
        val = pricingProblem(10,1,"AB")
        self.assertEqual(val, "$10.5")

    def test_case3(self):
        val = pricingProblem(6050,12.21,"AB")
        self.assertEqual(val, "$69807.62")

    def test_case4(self):
        val = pricingProblem(10000,2.25,"DE")
        self.assertEqual(val, "$20250.0")

    def test_case5(self):
        val = pricingProblem(8000,1,"QC")
        self.assertEqual(val, "$8554.14")

    def test_case6(self):
        val = pricingProblem(6000,1,"QC")
        self.assertEqual(val, "$6553.58")

if __name__=='__main__':
    unittest.main()