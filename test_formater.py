from unittest import TestCase
from main import Formater
import sys
sys.tracebacklimit = 0


class TestFormater(TestCase):
    def setUp(self):
        print(self._testMethodDoc)

    def tearDown(self):
        pass

    def test_clean_integers(self):
        """-- Test Clean Integers"""
        msg = "The correct numerical value is not being returned"
        self.assertEqual(Formater.clean_number('9, 000 000'), 9000000, msg=msg)
        self.assertEqual(Formater.clean_number('5'), 5, msg=msg)
        self.assertEqual(Formater.clean_number('58, 710, 520'), 58710520, msg=msg)

    def test_correct_int_cast(self):
        """-- Test Int Cast """
        msg = "The correct type is not being returned for the integers"
        self.assertIsInstance(Formater.clean_number('9, 000 000'), int, msg=msg)
        self.assertIsInstance(Formater.clean_number('5'), int)
        self.assertIsInstance(Formater.clean_number('58, 710, 520'), int, msg=msg)

    def test_clean_floats(self):
        pass

    def test_correct_float_cast(self):
        pass

    def test_comma_afther_dot(self):
        pass

    def test_multiple_dots(self):
        pass

    def test_no_valid_entrys(self):
        pass