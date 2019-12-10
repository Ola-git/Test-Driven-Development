import unittest
import email_address


class TestEmailAddress(unittest.TestCase):

    def test_is_correct(self):
        self.assertTrue(email_address.is_correct("olapyt@gmail.com"), "olapyt" + "@" + "gmail.com")