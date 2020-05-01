import unittest
from mean import *

class TestCode(unittest.TestCase):

    def test_mean(self):
        fun = mean([1,1])
        exp = 1
        self.assertEqual(fun, exp)
    def test_mean1(self):
        fun = mean([2,2])
        exp = 2
        self.assertEqual(fun ,exp)
if __name__ == '__main__':
    unittest.main()
