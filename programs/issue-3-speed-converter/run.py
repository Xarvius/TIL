def m_s_to_km_h(value):
    converted = value * 3.6
    return "{} m/s to {} km/h".format(value, converted)


def km_h_to_m_s(value):
    converted = value / 3.6
    return "{} km/h to {} m/s".format(value, converted)


def mile_h_to_km_h(value):
    converted = value * 1.609
    return "{} mile/h to {} km/h".format(value, converted)


def km_h_to_mile_h(value):
    converted = value / 1.609
    return "{} km/h to {} mile/h".format(value, converted)


def km_h_to_percent_light_speed(value):
    converted = value / 1.079e+9
    return "{} km/h to {}% speed of light".format(value, converted)


convert_dictionary = {
 1: {
     "input": "m/s",
     "output": "km/h",
     "equation": "value * 3.6"
 },
 2: {
     "input": "km/h",
     "output": "m/s",
     "equation": "value / 3.6"
 },
 3: {
     "input": "mile/h",
     "output": "km/h",
     "equation": "value * 1.609"
 },
 4: {
     "input": "km/h",
     "output": "mile/h",
     "equation": "value / 1.609"
 },
 5: {
     "input": "km/h",
     "output": "% prędkości światła",
     "equation": "value / 1.079e+9"},
}


def converter(value, equation, input, output):
    converted = eval(equation)
    print(value, input, "to", converted, output)


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
            answer = m_s_to_km_h(value)
        elif user_options == 2:
            answer = km_h_to_m_s(value)
        elif user_options == 3:
            answer = mile_h_to_km_h(value)
        elif user_options == 4:
            answer = km_h_to_mile_h(value)
        elif user_options == 5:
            answer = km_h_to_percent_light_speed(value)
        print(answer)
        if end_check():
            break


print("Program do konwersji prędkości w różnych jednostkach.", end="")
menu()
