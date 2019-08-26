import os
import random
import sys
import unittest

import array_hops


class Test_can_reach_the_end(unittest.TestCase):
    def setUp(self):
        self.can_reach_the_end = array_hops.can_reach_the_end

    def testGivenPassingExample(self):
        array = [1, 3, 1, 2, 0, 1]
        self.assertTrue(self.can_reach_the_end(array))

    def testGivenFailingExample(self):
        array = [1, 2, 1, 0, 0]
        self.assertFalse(self.can_reach_the_end(array))

    def testArrayWithOneLargeStep(self):
        array = [5, 0, 0, 0, 0, 0]
        self.assertTrue(self.can_reach_the_end(array))

    def testArrayWithSingleElement(self):
        array = [1]
        self.assertTrue(self.can_reach_the_end(array))

    def testArrayStartingWithZero(self):
        array = [0, 100, 300, 500]
        self.assertFalse(self.can_reach_the_end(array))

    def testArrayWithOneAndZeroAtStart(self):
        array = [1, 0, 25, 50, 50]
        self.assertFalse(self.can_reach_the_end(array))

    def testArrayWithHugeStartingStep(self):
        array = [50, 1, 2, 3, 4]
        self.assertTrue(self.can_reach_the_end(array))


if __name__ == '__main__':
    unittest.main()
