convert_dictionary = {
 1: [

     "m/s",
     "km/h",
     "value * 3.6"
 ],
 2: [
     "km/h",
     "m/s",
     "value / 3.6"
 ],
 3: [
     "mile/h",
     "km/h",
     "value * 1.609"
 ],
 4: [
     "km/h",
     "mile/h",
     "value / 1.609"
 ],
 5: [
     "km/h",
     "% prędkości światła",
     "value / 1.079e+9"
 ]
}

def converter(value, options):
    input, output, equation = options
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
            print(one, ")", list_one[0], "na", list_one[1])
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
