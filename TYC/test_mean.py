import unittest
from mean import *
import numpy as np

class TestCode(unittest.TestCase):

    def test_mean(self):
        fun = mean([1,1])
        exp = 1
        self.assertEqual(fun, exp)
    def test_mean1(self):
        fun = mean([2,2])
        exp = 2
        self.assertEqual(fun ,exp)
    def test_mean2(self):
        fun = mean([1,2])
        exp = 1.5
        self.assertEqual(fun, exp)
    def test_mean3(self):
        for i in range(0,100):
            for k in range(0,100):
                fun = mean([i,k])
                exp = np.mean([i,k]) 
                self.assertEqual(fun ,exp)
if __name__ == '__main__':
    unittest.main()
