from square_module import calculate_square_root, multiply, remove_vowels

if __name__ == "__main__":
    calculate_square_root()

import unittest


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(7, -3), -21)
        self.assertEqual(multiply(1.5, 2), 3.0)


class Testsremovevowels(unittest.TestCase):
    def test_remove_vowels(self):
        self.assertEqual(remove_vowels("banana"), "bnn")
        self.assertEqual(remove_vowels("example"), "xmpl")
        self.assertEqual(remove_vowels("AEIOU"), "")
        self.assertEqual(remove_vowels("Python"), "Pythn")
        self.assertEqual(remove_vowels(""), "")


if __name__ == "__main__":
    unittest.main()
