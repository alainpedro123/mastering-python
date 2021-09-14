# WITH STATEMENT - Shorter and cleaner way to release external resource connections, but it doesn't always work
# it works for certain kinds of objects
# "WITH" statement is used to automaticly released external resource connections

try:
    with open("appy.py") as file:
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didnn't enter a valid age.")
else:
    print("No exceptions were thrown.")

    # When working with multiples external resources. FOr example: Reading a data when one file and write it to another file

try:
    # with both of the external resources are gonna be automaticly relased
    with open("appy.py") as file, open("anotehr.txt") as target:
        print("File opened")

    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didnn't enter a valid age.")
else:
    print("No exceptions were thrown.")
