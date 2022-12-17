import unittest
from complex_numbers import Complex


class TestComplex(unittest.TestCase):

    def test_add(self):
        number_1 = Complex(2, 5)
        number_2 = Complex(2, 7)
        expected = Complex(4, 12)

        actual = number_1 + number_2

        self.assertEqual(str(expected), str(actual))

    def test_sub(self):
        number_1 = Complex(4, 5)
        number_2 = Complex(2, 9)
        expected = Complex(2, -4)

        actual = number_1 - number_2

        self.assertEqual(str(expected), str(actual))

    def test_mul(self):
        number_1 = Complex(2, 3)
        number_2 = Complex(5, 4)
        expected = Complex(-2, 23)

        actual = number_1 * number_2

        self.assertEqual(str(expected), str(actual))

    def test_truediv(self):
        number_1 = Complex(13, 1)
        number_2 = Complex(7, -6)
        expected = Complex(1.0, 1)

        actual = number_1 / number_2

        self.assertEqual(str(expected), str(actual))

    def test_abs(self):
        number = Complex(5, 12)
        expected = 13.0

        actual = abs(number)

        self.assertEqual(str(expected), str(actual))


if __name__ == "__main__":
    TestComplex()
