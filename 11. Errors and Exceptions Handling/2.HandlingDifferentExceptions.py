# 2. HANDLING DIFFERENT EXCEPTIONS - Errors

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except ValueError:
    print("You didnn't enter a valid age.")
except ZeroDivisionError:
    print("You didnn't enter a valid age.")
else:
    print("No exceptions were thrown.")


# specifying multiple types of Exceptions

try:
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didnn't enter a valid age.")

else:
    print("No exceptions were thrown.")