print("Greetings from file!")

def greeting_from_file():
    print("Greetings from file!")

greeting_from_file()

if __name__ == "__main__":
    pass
    # here you have a place to write code that will be
    # executed after python <path_to_this_script.py>

def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))

if __name__ == "__main__":
    customized_hello("John", "Cleese")

import sys

def customized_hello(first_name, last_name):
    print("Hello %s %s!" % (first_name, last_name))

if __name__ == "__main__":
    print(sys.argv)
    customized_hello("John", "Cleese")

print(sys.argv[1:])