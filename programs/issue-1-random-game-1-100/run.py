import random


def ask_and_check():
    rand_number = random.randint(1, 100)
    print("Została wylosowana liczba z przedziały 1-100.")
    print("Zgadnij jaka to liczba: ", end="")
    while True:
        try:
            answer = int(input())
        except ValueError:
            print("Gramy na int'ach! Podaj jeszcze raz: ", end="")
            continue
        if answer > rand_number:
            print("Za duża liczba.")
        elif answer < rand_number:
            print("Za mała liczba.")
        else:
            break
        print("Zgadnij jeszcze raz: ", end="")
    print("Tak! Brawo!")


ask_and_check()
