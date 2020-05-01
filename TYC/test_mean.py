import unittest
from mean import *

class TestCode(unittest.TestCase):

    def test_mean(self):
        fun = mean([1,1])
        exp = 1
        self.assertEqual(obs, exp)
