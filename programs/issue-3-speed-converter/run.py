convert_dictionary = {
 1: {
     "input": "m/s",
     "output": "km/h",
     "equation": "value * 3.6"},
 2: {
     "input": "km/h",
     "output": "m/s",
     "equation": "value / 3.6"},
 3: {
     "input": "mile/h",
     "output": "km/h",
     "equation": "value * 1.609"},
 4:  {
     "input": "km/h",
     "output": "mile/h",
     "equation": "value / 1.609"},
 5: {
     "input": "km/h",
     "output": "% prędkości światła",
     "equation": "value / 1.079e+9"}
}


def converter(value, options):
    try:
        input, output, equation = options["input"], options["output"], options["equation"]
    except ValueError:
        print("Coś poszło nie tak. Spróbuj ponownie później.")
        return
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
        for one in convert_dictionary:
            list_one = convert_dictionary[one]
            print(one, ")", list_one["input"], "na", list_one["output"])
        while True:
            try:
                user_options = int(input("Wybierz: "))
            except ValueError:
                print("Musisz podać numer opcji!")
                continue
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


print("Program do konwersji prędkości w różnych jednostkach.", end="")
menu()
