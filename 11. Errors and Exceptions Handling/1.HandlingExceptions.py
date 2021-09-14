# HANDLING EXCEPTION - Errors

try:
    from timeit import timeit
    age = int(input("Age: "))
except ValueError:
    print("You didnn't enter a valid age.")

else:
    print("No exceptions were thrown.")
print("Execution continues")


# Optional
try:
    age = int(input("Age: "))
except ValueError as ex:
    print("You didnn't enter a valid age.")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues")
