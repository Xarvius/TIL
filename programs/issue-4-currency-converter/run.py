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
    print(amount_currency, start_currency, "to", converted, end_currency)


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
        if end_check():
            break


print("Program do konwersji walut.")
menu()
