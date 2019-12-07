import unittest

import plik_kalkulator

class Test_Calculator(unittest.TestCase):

    def test_calculator(self):
        self.assertEqual(plik_kalkulator.dodaj(2,3), 5)
        self.assertEqual(plik_kalkulator.pomnoz(2,3), 6)
        self.assertEqual(plik_kalkulator.odejmij(22,2), 20)
        self.assertEqual(plik_kalkulator.podziel(33,11), 3)

if __name__=="__main__":  #to trzeba zapamietac#
    unittest.main()
