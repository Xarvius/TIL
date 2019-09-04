import random


def ask_and_check(rand_number):
    answer = int(input())
    if answer > rand_number:
        print("Za duża liczba.")
    elif answer < rand_number:
        print("Za mała liczba.")
    else:
        print("Tak! Brawo!")
        return 0
    print("Zgadnij jeszcze raz:")
    ask_and_check(rand_number)


number = random.randint(1, 100)
print("Została wylosowana liczba z przedziały 0-100.")
print("Zgadnij jaka to liczba: ")
ask_and_check(number)
