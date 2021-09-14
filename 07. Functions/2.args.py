# *args (arguments) 

# *args behaves like a tuple of parameters that are coming in.
# *args allows us to take random numbers of arguments.
# * means a collection of arguments

# EXAMPLE 1
def myfunc(*args):
  return sum(args)

myfunc(40,60,100)


# EXAMPLE 2
def myfunc(*args):
  for item in args:
    print(item)

myfunc(40,60,70,100)


# EXAMPLE 3
def multiply(*numbers):   # * means a collection of arguments
  total = 1
  for number in numbers:
    total *= number
  return total

print(multiply(2, 3, 4, 5))