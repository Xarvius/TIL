def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    print("{}°C to {}°F".format(celsius, fahrenheit))


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print("{}°F to {}°C".format(fahrenheit, celsius))


def menu():
    print("Program do konwersji temperatury w różnych skalach. Jaką konwersje chcesz wykonać?")
    print("1) Stopnie Celsjusza na Fahrenheita")
    print("2) Stopnie Fahrenheita na Celsjusza")
    while True:
        try:
            user_request = int(input("Wybierz: "))
        except ValueError:
            print("Musisz podać numer opcji!")
            continue
        if not 2 >= user_request >= 1:
            print("Nie istnieje taka opcja.")
            continue
        else:
            break
    while True:
        try:
            value = float(input("Podaj wartość: "))
        except ValueError:
            print("Musisz podać liczbę!")
            continue
        break
    if user_request == 1:
        celsius_to_fahrenheit(value)
    elif user_request == 2:
        fahrenheit_to_celsius(value)


menu()