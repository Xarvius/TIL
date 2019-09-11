from unittest import TestCase
from run import currency_converter


class TestCurrency_converter(TestCase):
    def test_currency_converter(self):
        self.assertEqual(currency_converter("PLN", "EUR", 1), 0.23)

    def test_currency_converter_bad_start(self):
        self.assertEqual(currency_converter("badCurrency", "EUR", 1), "HttpError")

    def test_currency_converter_bad_end(self):
        self.assertEqual(currency_converter("PLN", "badCurrency", 1), "KeyError")
