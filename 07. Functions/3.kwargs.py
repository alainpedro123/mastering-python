# **kwargs (keywords arguments)
# It builds a Dictionary of key value pairs.

# EXAMPLE1
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print('My fruit of choice is {}'.format(kwargs['fruit']))
  else:
    print('I did not find any fruit here')

myfunc(fruit='apple')
myfunc(fruit='mongo', veggie="lettuce")


# EXAMPLE 2
# a) It returns a Dictionary
def myfunc(**kwargs):
  if 'fruit' in kwargs:
    print(kwargs)

myfunc(fruit='apple', veggie="lettuce")


# b) 
def myfunc(*args, **kwargs):
  print('I would like {}{}'.format(args[0],kwargs['fruit']))
  print(args)
  print(kwargs)
myfunc(10,20,30,fruit='orange', food="eggs", animal="dog")

# *args (arguments) and **kwargs (keywords arguments)


# EXAMPLE 3
def save_user(**user):
  print(user)
  print(user["id"])
  print(user["name"])
save_user(id=1, name="John", age=22)