import sys

def print_maturity(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a kiddo!")

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)

print("The program was called with this parameters %s" % sys.argv[1:])
print("The first parameter is %s" % sys.argv[1])

text = {"John, Livia, Mark, Stephen"}

with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)

new_name = "Luke"
with open("names.txt", 'a') as write_file:
    write_file.write(new_name)

new_name = "Luke"
with open("new_names.txt", 'w') as write_file:
    write_file.write(new_name)