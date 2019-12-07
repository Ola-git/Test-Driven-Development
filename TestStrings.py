import unittest
import program

class Test_Str_methods():

    def test_upper(self):
        self.assertEqual(program.doUpper("ala ma kota"), "ALA MA KOTA")

    def test_capitalise(self):
        self.assertEqual(program.doCapitalise("ola"), "Ola")

    def test_replace(self):
        str = program.doReplace("co", "na co")
        self.assertTrue(str.index("na co") > 0)

    def test_lower(self):
        self.assertEqual(program.doLower("QWERTY"), "qwerty")

    def test_startswith(self):
        self.assertEqual(program.doStartswith("Ala ma kota"), "Ala")

if __name__=="__main__":  #to trzeba zapamietac#
    unittest.main()
