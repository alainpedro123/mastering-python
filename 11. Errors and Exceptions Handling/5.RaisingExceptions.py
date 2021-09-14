# RAISING EXCEPTIONS - NOT RECOMMENDED!

# 1. Raising exceptions
def calculate_xgactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10/age


# 2. Handling it in below function
try:
    calculate_xgactor(-1)
except ValueError as error:
    print(error)