# FINALLY

try:
    file = open("appy.py")
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didnn't enter a valid age.")
else:
    print("No exceptions were thrown.")
finally:   # That's the suitable place to close external resource connections
    file.close()