import unittest

from palindrome import ispalindrome
from palindrome import reverse


class TestPalindrome(unittest.TestCase):
    def test_palindrome(self):
        one = ispalindrome("anna")
        two = reverse("anna")
