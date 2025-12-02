import unittest
import functions

class TestMinutes(unittest.TestCase):
    def test_that_get_hours_exists(self):
        functions.get_hours(130)
    def test_that_get_hours_function_returns_correct_value(self):
        actual = functions.get_hours(130)
        expected = 2,10
        self.assertEqual(actual,expected)
        actual = functions.get_hours(120)
        expected = 2
        self.assertEqual(actual,expected)
