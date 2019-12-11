import unittest
import email_address


class TestEmailAddress(unittest.TestCase):

    def test_is_correct1(self):
        self.assertTrue(email_address.is_correct1("olapyt@gmail.com"), "olapyt" + "@" + "gmail.com")

    def test_is_correct2(self):
        self.assertTrue(email_address.is_correct2("olapyt@gmail.com"), ".")