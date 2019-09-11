import requests
from unittest import TestCase
from run import currency_converter


class TestCurrencyConverter(TestCase):
    def test_currency_converter(self):
        start, end, currency = "PLN", "EUR", 1
        param = {
            "base": start
        }
        response = requests.get("https://api.exchangeratesapi.io/latest", params=param)
        currency_rates = response.json()["rates"][end]
        converted = round(currency * currency_rates, 2)
        self.assertEqual(currency_converter(start, end, currency), converted)

    def test_currency_converter_bad_start(self):
        self.assertEqual(currency_converter("badCurrency", "EUR", 1), "HttpError")

    def test_currency_converter_bad_end(self):
        self.assertEqual(currency_converter("PLN", "badCurrency", 1), "KeyError")
