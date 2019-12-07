import unittest
import mojprogram

class TestTDD(unittest.TestCase):

    def test_zwroc_100(self):

        wynik = mojprogram.zwroc_100()
        self.assertEqual(wynik, 100)

    def test_zwroc_parametr(self):
        self.assertEqual(mojprogram.zwroc_parametr(124), 124)

    

if __name__=="__main__":  #to trzeba zapamietac#
    unittest.main()
