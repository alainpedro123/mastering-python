# COST OF RAISING EXCEPTIONS

# 1. calcualting the execution time of the code below:
code1 = """
def calculate_xfactor(age):
  if age <= 0:
    raise ValueError("Age cannot be 0 or less")  
  return 10/age

try:
  calculate_xfactor(-1)
except ValueError as error:
  print(error)
"""

# number -> this function will execute out python code "number" times. It will calculate the execution time and return it
print("first code= ", timeit(code1, number=100))


# 2. calcualting the execution time of the code below - using "pass"
code1 = """
def calculate_xfactor(age):
  if age <= 0:
    raise ValueError("Age cannot be 0 or less")  
  return 10/age

try:
  calculate_xfactor(-1)
except ValueError as error:
  pass
"""

print("second code= ", timeit(code1, number=100))


# 3. returning a value like "None" - which is an object tha represents an absence of a value
code1 = """
def calculate_xfactor(age):
  if age <= 0:
    return None
  return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None: 
  pass
"""

print("third code= ", timeit(code1, number=100))
