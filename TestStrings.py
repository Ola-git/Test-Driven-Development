import unittest
import program

class Test_Str_methods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(program.doUpper("ala ma kota"), "ALA MA KOTA")

    def test_capitalize(self):
        self.assertEqual(program.doCapitalize("ola"), "Ola")

    def test_replace(self):
        str = program.doReplace("bananas", "apples", "I like bananas")
        self.assertTrue(str.index("apples") > 0)

    def test_lower(self):
        self.assertEqual(program.doLower("QWERTY"), "qwerty")

    def test_startswith(self):
        self.assertTrue(program.doStartswith("Ala ma kota"), "Ala")

if __name__=="__main__":  #to trzeba zapamietac#
    unittest.main()
