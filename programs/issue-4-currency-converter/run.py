import requests


def currency_converter(start_currency, end_currency, amount_currency):
    param = {
        "base": start_currency
    }
    response = requests.get("https://api.exchangeratesapi.io/latest", params=param)
    try:
        currency_rates = response.json()["rates"][end_currency]
    except KeyError:
        print("Wystąpił błąd, spróbuj ponownie. W przypadku powtórzenia się błedu, spróbuj później.")
        return
    converted = amount_currency * currency_rates
    print("{} {} to {} {}".format(amount_currency, start_currency, converted, end_currency))


def menu():
    print("Dostępne waluty: PLN, EUR, USD, CHF, CNY.")
    start_currency = input("Wybierz pierwszą walutę: ")
    end_currency = input("Wybierz drugą walutę: ")
    while True:
        try:
            amount_currency = float(input("Podaj kwotę w walucie {}: ".format(start_currency)))
            break
        except ValueError:
            print("Musisz podać liczbę!")
            continue
    print("Trwa sprawdzanie kursu...")
    currency_converter(start_currency, end_currency, amount_currency)


print("Program do konwersji walut.")
menu()
