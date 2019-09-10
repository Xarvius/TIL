convert_dictionary = {
 "1": {
     "input": "m/s",
     "output": "km/h",
     "equation": lambda value: value * 3.6,
 },
 "2": {
     "input": "km/h",
     "output": "m/s",
     "equation": lambda value: value / 3.6,
 },
 "3": {
     "input": "mile/h",
     "output": "km/h",
     "equation": lambda value: value * 1.609,
 },
 "4":  {
     "input": "km/h",
     "output": "mile/h",
     "equation": lambda value: value / 1.609,
 },
 "5": {
     "input": "km/h",
     "output": "% prędkości światła",
     "equation": lambda value: value / 1.079e+9,
 },
}


def converter(value, options):
    try:
        input_type, output_type, equation = options["input"], options["output"], options["equation"]
    except KeyError:
        print("Coś poszło nie tak. Spróbuj ponownie później.")
        return
    print(value, input_type, "to", equation(value), output_type)


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
        for one in convert_dictionary:
            list_one = convert_dictionary[one]
            print(one, ")", list_one["input"], "na", list_one["output"])
        while True:
            user_options = input("Wybierz: ")
            try:
                user_options = convert_dictionary[user_options]
            except KeyError:
                print("Nie istnieje taka opcja.")
                continue
            break
        while True:
            try:
                value = float(input("Podaj wartość: "))
            except ValueError:
                print("Musisz podać liczbę!")
                continue
            break
        converter(value, user_options)
        if end_check():
            break


print("Program do konwersji prędkości w różnych jednostkach.", end=" ")
menu()
