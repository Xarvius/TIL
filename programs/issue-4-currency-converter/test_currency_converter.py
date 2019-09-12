import unittest
from unittest import TestCase
from unittest.mock import patch
from run import get_rates_from_exchangeratesapi_io, converter_main


class TestCurrencyConverter(TestCase):
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
        with patch('run.requests.get') as mock_get:
            mock_get.return_value.json.return_value = mock_list
            response = get_rates_from_exchangeratesapi_io("EUR")
        self.assertIn("PLN", response)

    def test_get_rates_from_exchangeratesapi_io_connection_fail(self):
        with patch('run.requests.get') as mock_get:
            mock_get.side_effect = ConnectionError
            converter_main("PLN", "EUR", 1)
        self.assertRaises(ConnectionError)

    def test_get_rates_from_exchangeratesapi_io_timeout_fail(self):
        with patch('run.requests.get') as mock_get:
            mock_get.side_effect = TimeoutError
            converter_main("PLN", "EUR", 1)
        self.assertRaises(TimeoutError)


if __name__ == '__main__':
    unittest.main()
