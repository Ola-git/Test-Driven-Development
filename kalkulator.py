import unittest

import plik_kalkulator

class Test_Calculator(unittest.TestCase):

    def test_calculator_dodaj(self):
        self.assertEqual(plik_kalkulator.dodaj(2,3), 5)

    def test_calculator_pomnoz(self):
        self.assertEqual(plik_kalkulator.pomnoz(2,3), 6)

    def test_calculator_odejmij(self):
        self.assertEqual(plik_kalkulator.odejmij(22,2), 20)

    def test_calculator_podziel(self):
        self.assertEqual(plik_kalkulator.podziel(33,11), 3)

if __name__=="__main__":  #to trzeba zapamietac#
    unittest.main()
