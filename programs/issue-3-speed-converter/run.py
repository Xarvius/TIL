def m_s_to_km_h():
    pass


def km_h_to_m_s():
    pass


def km_h_to_mile_h():
    pass


def km_h_to_percent_light_speed():
    pass


def menu():
    print("Jaką konwersje chcesz wykonać?")
    print("1) m/s na km/h")
    print("2) km/h na m/s")
    print("3) mile/h na km/h")
    print("4) km/h na mile/h")
    print("5) km/h na procent prędkości światła w próźni")
    while True:
        try:
            user_options = int(input("Wybierz: "))
        except ValueError:
            print("Musisz podać numer opcji!")
            continue
        if not 1 <= user_options <= 5:
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
    if user_options == 1:
        pass
    elif user_options == 2:
        pass
    elif user_options == 3:
        pass
    elif user_options == 4:
        pass
    elif user_options == 5:
        pass
    print("answer")



print("Program do konwersji prędkości w różnych jednostkach.", end="")
menu()
