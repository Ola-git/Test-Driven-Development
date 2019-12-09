import unittest
import test_email_address


class TestEmailAddress(unittest.TestCase):

    def test_is_correct(self):
        self.assertTrue("olapyt@gmail.com", "olapyt" + "@" + "gmail" + "." + "com")