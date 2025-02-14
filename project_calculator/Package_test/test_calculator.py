import unittest
import logging

from Calculator.Package_Calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the test fixture before exercising the test."""
        self.calc = Calculator()
        self.log = logging.getLogger()

    def test_add_integers(self):
        """Test the add method with valid integers."""
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.log.warning("Test somme 2 entier OK")

    def test_add_non_integers(self):
        """Test the add method with non-integer inputs."""
        self.assertEqual(self.calc.add(1, '2'), "ERROR")
        self.assertEqual(self.calc.add('1', 2), "ERROR")
        self.assertEqual(self.calc.add('1', '2'), "ERROR")
        self.log.warning("test somme entier et non entier OK")

    def test_subtract_integers(self):
        """Test the subtract method with valid integers."""
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.log.warning("Test différence 2 entier OK")

    def test_subtract_non_integers(self):
        """Test the subtract method with non-integer inputs."""
        self.assertEqual(self.calc.subtract(2, '1'), "ERROR")
        self.assertEqual(self.calc.subtract('2', 1), "ERROR")
        self.assertEqual(self.calc.subtract('2', '1'), "ERROR")
        self.log.warning("test différence entier et non entier OK")

    def test_multiply_integers(self):
        """Test the multiply method with valid integers."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.log.warning("Test multiplication 2 entier OK")

    def test_multiply_non_integers(self):
        """Test the multiply method with non-integer inputs."""
        self.assertEqual(self.calc.multiply(2, '3'), "ERROR")
        self.assertEqual(self.calc.multiply('2', 3), "ERROR")
        self.assertEqual(self.calc.multiply('2', '3'), "ERROR")
        self.log.warning("test multiplication entier et non entier OK")

    def test_divide_integers(self):
        """Test the divide method with valid integers."""
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertEqual(self.calc.divide(-6, -3), 2)
        self.log.warning("Test division 2 entier OK")

    def test_divide_non_integers(self):
        """Test the divide method with non-integer inputs."""
        self.assertEqual(self.calc.divide(6, '3'), "ERROR")
        self.assertEqual(self.calc.divide('6', 3), "ERROR")
        self.assertEqual(self.calc.divide('6', '3'), "ERROR")
        self.log.warning("test division entier et non entier OK")

    def test_divide_by_zero(self):
        """Test the divide method with zero as the divisor."""
        self.assertEqual(self.calc.divide(1, 0), "Impossible de diviser par zéro")
        self.log.warning("Test division par 0 OK")


if __name__ == '__main__':
    unittest.main()

