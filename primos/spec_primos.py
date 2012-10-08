import unittest
from should_dsl import should, should_not, matcher
from primos import primos


class TestPrimos(unittest.TestCase):

	def test_tres_e_primo(self):
		primos(3) |should| equal_to(True)

	def test_quatro_nao_e_primo(self):
		primos(4) |should| equal_to(False)

	def test_cinco_e_primo(self):
		primos(5) |should| equal_to(True)
	
	def test_quinze_nao_e_primo(self):
		primos(15) |should| equal_to(False)

	def test_um_nao_e_primo(self):
		primos(1) |should| equal_to(False)

	def test_zero_nao_e_primo(self):
		primos(0) |should| equal_to(False)