import unittest
from should_dsl import should
from fibonacci import fibonacci


class TestFibonacci(unittest.TestCase):

	def test_fibonacci_um(self):
		fibonacci(1) |should| equal_to([0])

	def test_fibonacci_dois(self):
		fibonacci(2) |should| equal_to([0, 1])

	def test_fibonacci_tres(self):
		fibonacci(3) |should| equal_to([0, 1, 1])		

	def test_fibonacci_quatro(self):
		fibonacci(4) |should| equal_to([0, 1, 1, 2])

	def test_fibonacci_dez(self):
		fibonacci(10) |should| equal_to([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])