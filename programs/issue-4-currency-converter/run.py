import requests
from constants import CURRENCY_URL

def currency_converter(start_currency, end_currency, amount_currency):
    param = {
        "base": start_currency
    }
    try:
        response = requests.get(CURRENCY_URL, params=param)
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print("Nie znaleziono waluty: {}".format(start_currency))
        return "HttpError"
    except requests.exceptions.ConnectionError as err:
        print("Wystąpił błąd. Sprawdź połaczenie z internetem.")
        return "ConnectionError"
    except requests.exceptions.Timeout as err:
        print("Przekroczono czas oczekiwania na odpowiedź. Spróbuj ponownie później.")
        return "Timeout"

    try:
        currency_rates = response.json()["rates"][end_currency]
    except KeyError as err:
        print("Nie znaleziono waluty: {}".format(end_currency))
        return "KeyError"

    converted = round(amount_currency * currency_rates, 2)
    print(amount_currency, start_currency, "to", converted, end_currency)
    return converted


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
        currency_converter(start_currency, end_currency, amount_currency)
        if end_check():
            break


#print("Program do konwersji walut.")
#menu()
