import requests
from unittest import TestCase
from run import currency_converter


class TestCurrencyConverter(TestCase):
    def test_currency_converter(self):
        param = {
            "base": "PLN"
        }
        response = requests.get("https://api.exchangeratesapi.io/latest", params=param)
        currency_rates = response.json()["rates"]["EUR"]
        converted = round(1 * currency_rates, 2)
        self.assertEqual(currency_converter("PLN", "EUR", 1), converted)

    def test_currency_converter_bad_start(self):
        self.assertEqual(currency_converter("badCurrency", "EUR", 1), "HttpError")

    def test_currency_converter_bad_end(self):
        self.assertEqual(currency_converter("PLN", "badCurrency", 1), "KeyError")
