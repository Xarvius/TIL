import requests
from constants import CURRENCY_API


def error_handler(err, response):
    pass


def converter_main(start_currency, end_currency, amount_currency):
    try:
        response = get_rates(start_currency, end_currency)
        end_currency_value = get_end_rate(response, end_currency)
        converter_currency(start_currency, end_currency, amount_currency, end_currency_value)
    except (ValueError, ConnectionError, TimeoutError, KeyError) as err:
        error_handler(err, response)


def converter_currency(start_currency, end_currency, amount_currency, response):
    converted = round(amount_currency * response, 2)
    print(amount_currency, start_currency, "to", converted, end_currency)


def get_rates(start_currency, end_currency):
    if CURRENCY_API == 'https://api.exchangeratesapi.io/latest':
        return get_rates_from_exchangeratesapi_io(start_currency, end_currency)
    else:
        raise NameError


def get_rates_from_exchangeratesapi_io(start_currency, end_currency):
    param = {
        "base": start_currency
    }
    try:
        response = requests.get(CURRENCY_API, params=param)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        raise ValueError
    except requests.exceptions.ConnectionError:
        raise ConnectionError
    except requests.exceptions.Timeout:
        raise TimeoutError
    return response.json()["rates"]


def get_end_rate(rates, end_currency):
    try:
        return rates[end_currency]
    except KeyError as Err:
        raise Err


def end_check():
    while True:
        user_options = input("Czy zakończyć program ([T]ak/[N]ie)? ")
        upper_user_options = user_options.upper()
        if upper_user_options == "TAK" or upper_user_options == "T":
            return True
        elif upper_user_options == "NIE" or upper_user_options == "N":
            return False


def menu():
    while True:
        print("Dostępne waluty: PLN, EUR, USD, CHF, CNY...")
        start_currency = input("Wybierz pierwszą walutę: ").upper()
        end_currency = input("Wybierz drugą walutę: ").upper()
        while True:
            try:
                amount_currency = float(input("Podaj kwotę w walucie {}: ".format(start_currency)))
                break
            except ValueError:
                print("Musisz podać liczbę!")
                continue
        print("Trwa sprawdzanie kursu...")
        converter_main(start_currency, end_currency, amount_currency)
        if end_check():
            break


print("Program do konwersji walut.")
menu()
