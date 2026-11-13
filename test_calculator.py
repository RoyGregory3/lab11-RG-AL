import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
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