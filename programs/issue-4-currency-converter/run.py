def currency_converter():
    pass


def menu():
    print("Dostępne waluty: PLN, EUR, USD, CHF, CNY.")
    start_currency = input("Wybierz pierwszą walutę: ")
    end_currency = input("Wybierz drugą walutę: ")
    while True:
        try:
            amount_currency = int(input("Podaj kwotę w walucie {}: ".format(start_currency)))
            break
        except ValueError:
            print("Musisz podać liczbę!")
            continue
    print("Trwa sprawdzanie kursu...")
    currency_converter()
    

print("Program do konwersji walut.")
menu()
