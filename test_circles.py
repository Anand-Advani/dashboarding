import unittest
from circles import circle_area
from math import pi

class TestCircleArea(unittest.TestCase):
	def test_area(self):
		#Test areas when radius>=0
		#1st arg = our op , 2nd arg = correct value
		self.assertAlmostEqual(circle_area(1),pi)
		self.assertAlmostEqual(circle_area(0),0)
		self.assertAlmostEqual(circle_area(2.1),pi*2.1**2)

	def test_values(self):
		#To make sure value errors are raised when necessary
		#arg sequence - exception name , function name , args
		self.assertRaises(ValueError,circle_area,-2)

	def test_types(self):
		#To make sure type errors are raised when necessary
		self.assertRaises(TypeError,circle_area,3+5j)
		

"""
Now run this file from cli as 
python -m unittest test_circles
OR
python -m unittest   ----to run all test files indeed
-m instructs python to run unittest module as script
"""
