print("Welcome to calculator")
import logging
def calculate(choice):
    if choice == "1":
        logging.info("Dodajemy")
        num1 = input("Enter the first number")
        num2 = input("Enter the second number") 
        return int(num1) + int(num2)
    if choice == "2":
        logging.info("Obejmójemy")
        num1 = input("Enter the first number")
        num2 = input("Enter the second number") 
        return int(num1) - int(num2)
    if choice == "3":
        logging.info("Mnozymy")
        num1 = input("Enter the first number")
        num2 = input("Enter the second number") 
        return int(num1) * int(num2)
    if choice == "4":
        logging.info("Dzielimy")
        num1 = input("Enter the first number")
        num2 = input("Enter the second number") 
        return int(num1) / int(num2) if "0" != 0 else "Error, division by 0 is impossible."
choice = input("Choose 1 - Add 2 - Subtract 3 - Multiply 4 - Divide")
result = calculate(choice)

print(result)