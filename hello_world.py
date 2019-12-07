import unittest

import mojprogram1

class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):
        self.assertEqual(mojprogram1.hello_world(), "Hello World")

if __name__=="__main__":  #to trzeba zapamietac#
    unittest.main()
