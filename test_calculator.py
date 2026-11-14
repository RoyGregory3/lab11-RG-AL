import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(0,0), 0)
        self.assertEqual(add(2,3), 5)
        self.assertEqual(add(-5,10), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(5,3), 2)
        self.assertEqual(sub(0,0), 0)
        self.assertEqual(sub(-5,10), -15)
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0,0),0)
        self.assertEqual(mul(2.56,7.0),17.92)
        self.assertEqual(mul(12345,-6789), -83810205)

    def test_divide(self):
        self.assertEqual(div(-1,10), -10)
        self.assertEqual(div(5,0),0)
        self.assertAlmostEqual(div(3,10),3.33, places = 2)
    ##########################


    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2,8), 3)
        self.assertEqual(log(10,100), 2)
        self.assertEqual(log(3,81), 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(1, 5)
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(1,0), 1)
        self.assertEqual(hypotenuse(3.0,-4.0),5.0)
        self.assertAlmostEqual(hypotenuse(1.0,1.0),1.41, places = 2)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(0),0)
        self.assertAlmostEqual(square_root(2), 1.41, places = 2)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()