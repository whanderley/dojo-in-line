import unittest
from should_dsl import should
from numeros_felizes import eh_feliz


class TestNumeroFeliz(unittest.TestCase):

	def test_sete_e_feliz(self):
		eh_feliz(7) |should| equal_to(True)

	def test_quatro_nao_e_feliz(self):
		eh_feliz(4) |should| equal_to(False)

	def test_dez_e_feliz(self):
		eh_feliz(10) |should| equal_to(True)

	def test_dois_nao_e_feliz(self):
		eh_feliz(2) |should| equal_to(False)


if __name__ == '__main__':
	unittest.main()