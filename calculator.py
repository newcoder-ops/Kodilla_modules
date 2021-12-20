print("Welcome to calculator")
import logging
def calculate(choice):
    if choice == "1":
        logging.info("Dodajemy")
        a = input("Podaj pierwszą liczbę")
        b = input("Podaj drugą liczbę")
        return int(a) + int(b)
    if choice == "2":
        logging.info("Obejmójemy")
        a = input("Podaj pierwszą liczbę")
        b = input("Podaj drugą liczbę")
        return int(a) - int(b)
    if choice == "3":
choice = input("Wybierz 1 - dodawanie 2 - odejmowanie")
result = calculate(choice)

print(result)