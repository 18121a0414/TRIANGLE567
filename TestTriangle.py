# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(7, 9, 12), 'Scalene', '7,9,12 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Scalene', '8,15,17 is a Scalene triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(6, 6, 10), 'Isosceles', '6,6,10 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(9, 12, 9), 'Isosceles', '9,12,9 is an Isosceles triangle')

    def testInvalidTriangleA(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')

    def testInvalidTriangleB(self):
        self.assertEqual(classifyTriangle(0, 5, 5), 'InvalidInput', '0,5,5 is invalid input')

    def testNegativeSidesA(self):
        self.assertEqual(classifyTriangle(-2, -3, -4), 'InvalidInput', '-2,-3,-4 is invalid input')

    def testNegativeSidesB(self):
        self.assertEqual(classifyTriangle(5, -12, 13), 'InvalidInput', '5,-12,13 is invalid input')

    def testZeroSidesA(self):
        self.assertEqual(classifyTriangle(0, 0, 0), 'InvalidInput', '0,0,0 is invalid input')

    def testZeroSidesB(self):
        self.assertEqual(classifyTriangle(5, 0, 5), 'InvalidInput', '5,0,5 is invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

