from unittest import TestCase

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
