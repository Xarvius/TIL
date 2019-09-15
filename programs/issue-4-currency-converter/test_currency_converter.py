import unittest
from unittest.mock import patch
from run import get_rates_from_exchangeratesapi_io, converter_main
import io
import sys


class TestCurrencyConverter(unittest.TestCase):
    def test_get_rates_from_exchangeratesapi_io(self):
        mock_list = {
            "rates":
            {
                "PLN": 4.3335,
                "USD": 1.1003,
            },
            "base": "EUR",
            "date": "2019-09-11",
        }
        with unittest.mock.patch('run.requests.get') as mock_get:
            mock_get.return_value.json.return_value = mock_list
            response = get_rates_from_exchangeratesapi_io("EUR")
        self.assertIn("PLN", response)

    def test_converter_main_connectionerror(self):
        with unittest.mock.patch('run.requests.get') as mock_get:
            mock_get.side_effect = ConnectionError
            print_catch = io.StringIO()
            old = sys.stdout
            sys.stdout = print_catch
            converter_main("PLN", "EUR", 1)
            sys.stdout = old
        self.assertEqual(print_catch.getvalue(), "Wystąpił błąd połączenia, spróbuj ponownie później.\n")


if __name__ == '__main__':
    unittest.main()
