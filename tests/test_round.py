from unittest import TestCase
import math

import saneround as sr

class RoundTest(TestCase):
    def test_simple_case(self) -> None:
        self.assertEqual(sr.round(0.4), 0.0)
        self.assertEqual(sr.round(0.5), 1.0)
        self.assertEqual(sr.round(1.4), 1.0)
        self.assertEqual(sr.round(1.5), 2.0)
        self.assertEqual(sr.round(2.4), 2.0)
        self.assertEqual(sr.round(2.5), 3.0)

        self.assertEqual(sr.round(-0.4), 0.0)
        self.assertEqual(sr.round(-0.5), -1.0)
        self.assertEqual(sr.round(-1.4), -1.0)
        self.assertEqual(sr.round(-1.5), -2.0)
        self.assertEqual(sr.round(-2.4), -2.0)
        self.assertEqual(sr.round(-2.5), -3.0)

        self.assertEqual(sr.round(0.0), 0.0)

    def test_near_limit(self) -> None:
        self.assertEqual(sr.round(0.49999999999999994), 0.0)
        self.assertEqual(sr.round(-0.49999999999999994), 0.0)

    def test_round_inf(self) -> None:
        self.assertEqual(sr.round(math.inf), math.inf)
        self.assertEqual(sr.round(-math.inf), -math.inf)
        self.assertEqual(sr.round(math.inf, 2), math.inf)
        self.assertEqual(sr.round(-math.inf, 2), -math.inf)
        self.assertEqual(sr.round(math.inf, -2), math.inf)
        self.assertEqual(sr.round(-math.inf, -2), -math.inf)

    def test_round_nan(self) -> None:
        self.assertTrue(math.isnan(sr.round(math.nan)))
        self.assertTrue(math.isnan(sr.round(math.nan, 2)))
        self.assertTrue(math.isnan(sr.round(math.nan, -2)))

    def test_ndigits(self) -> None:
        self.assertEqual(sr.round(5.5, 0), 6.0)
        self.assertEqual(sr.round(5.7, 1), 5.7)
        self.assertEqual(sr.round(1.2345678, 2), 1.23)
        self.assertEqual(sr.round(123456.78, -2), 123500)
        self.assertEqual(sr.round(-123456.78, -2), -123500)
        self.assertEqual(sr.round(12.345678, 3), 12.346)
        self.assertEqual(sr.round(0.8346268, -1), 0)

        self.assertEqual(sr.round(24999, -4), 20000)
        self.assertEqual(sr.round(25000, -4), 30000)
        self.assertEqual(sr.round(-24999, -4), -20000)
        self.assertEqual(sr.round(-25000, -4), -30000)

        self.assertEqual(sr.round(1.254999, 2), 1.25)
        self.assertEqual(sr.round(1.255, 2), 1.26)
        self.assertEqual(sr.round(5.014999, 2), 5.01)
        self.assertEqual(sr.round(5.015, 2), 5.02)
        self.assertEqual(sr.round(-1.254999, 2), -1.25)
        self.assertEqual(sr.round(-1.255, 2), -1.26)
        self.assertEqual(sr.round(-5.014999, 2), -5.01)
        self.assertEqual(sr.round(-5.015, 2), -5.02)

    def test_hard_case(self) -> None:
        # https://bugs.ruby-lang.org/issues/5227
        self.assertEqual(sr.round(42.0, 308), 42.0)
        self.assertEqual(sr.round(1.0e307, 2), 1.0e307)

        # https://bugs.ruby-lang.org/issues/5271
        self.assertEqual(sr.round(0.42, 2**30), 0.42)
        self.assertEqual(sr.round(0.42, -2**30), 0.0)

        # https://bugs.ruby-lang.org/issues/5272
        self.assertEqual(sr.round(2.5e20, -20), 3.0e20)
        self.assertEqual(sr.round(2.4e20, -20), 2.0e20)
        self.assertEqual(sr.round(-2.5e20, -20), -3.0e20)
        self.assertEqual(sr.round(-2.4e20, -20), -2.0e20)
        self.assertEqual(sr.round(2.5e200, -200), 3.0e200)
        self.assertEqual(sr.round(2.4e200, -200), 2.0e200)
        self.assertEqual(sr.round(-2.5e200, -200), -3.0e200)
        self.assertEqual(sr.round(-2.4e200, -200), -2.0e200)

        # https://bugs.ruby-lang.org/issues/5228
        self.assertEqual(sr.round(25 * (10 ** 70) - 1, -71), 2.0e71)
        #self.assertEqual(sr.round(25 * (10 ** 70), -71), 3.0e71)   # FIXME
        self.assertEqual(sr.round(-25 * (10 ** 70) + 1, -71), -2.0e71)
        #self.assertEqual(sr.round(-25 * (10 ** 70), -71), -3.0e71) # FIXME

        # https://bugs.ruby-lang.org/issues/14635
        #self.assertEqual(sr.round(3.0e-31, 31), 3.0e-31)   # FIXME
        #for i in range(1, 32): # FIXME
        for i in range(1, 16):
            self.assertEqual(sr.round(0.5, i), 0.5)
