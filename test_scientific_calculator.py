import unittest
import math
from scientific_calculator import sin, cos, tan, sqrt, log, exp

class ScientificCalculatorTest(unittest.TestCase):

    def test_sin_positive(self):
        self.assertAlmostEqual(sin(90), 1.0)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-90), -1.0)

    def test_sin_zero(self):
        self.assertAlmostEqual(sin(0), 0.0)

    def test_sin_non_numeric(self):
        with self.assertRaises(TypeError):
            sin("hello")

    def test_cos_positive(self):
        self.assertAlmostEqual(cos(90), 0.0)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(-90), 0.0)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos(0), 1.0)

    def test_cos_non_numeric(self):
        with self.assertRaises(TypeError):
            cos("hello")

    def test_tan_positive(self):
        self.assertAlmostEqual(tan(45), 1.0)

    def test_tan_negative(self):
        self.assertAlmostEqual(tan(-45), -1.0)

    def test_tan_zero(self):
        self.assertAlmostEqual(tan(0), 0.0)

    def test_tan_non_numeric(self):
        with self.assertRaises(TypeError):
            tan("hello")

    def test_sqrt_positive(self):
        self.assertAlmostEqual(sqrt(4), 2.0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-1)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(sqrt(0), 0.0)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(TypeError):
            sqrt("hello")

    def test_log_positive(self):
        self.assertAlmostEqual(log(10), 1.0)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log(-1)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_log_non_numeric(self):
        with self.assertRaises(TypeError):
            log("hello")

    def test_exp_positive(self):
        self.assertAlmostEqual(exp(2), math.exp(2))

    def test_exp_negative(self):
        self.assertAlmostEqual(exp(-2), math.exp(-2))

    def test_exp_zero(self):
        self.assertAlmostEqual(exp(0), 1.0)

    def test_exp_non_numeric(self):
        with self.assertRaises(TypeError):
            exp("hello")

if __name__ == '__main__':
    unittest.main()

