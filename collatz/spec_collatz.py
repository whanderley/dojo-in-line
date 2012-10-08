import unittest
from should_dsl import should
from collatz import collatz


class TestCollatz(unittest.TestCase):

	def spec_collatz_treze(self):
		collatz(13) |should| equal_to([13, 40, 20, 10, 5, 16, 8, 4, 2, 1])

	def spec_collatz_cinco(self):
		collatz(5) |should|	equal_to([5, 16, 8, 4, 2, 1])
	
	def spec_collatz_dez(self):
		collatz(10) |should| equal_to([10, 5, 16, 8, 4, 2, 1])	