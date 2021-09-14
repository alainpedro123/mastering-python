### 21. GENERATOR OBJECTS - are iterable, just like lists we can iterate over them, in each iteration we generate or spit out
# a new value. They don't store all the value in the memory, so we won't be able to get all the items we're working with 
# They generate a new value in each iteration returning even number from 0 to 18

from sys import getsizeof

# List 
values = [x * 2 for x in range(10)]
for x in values:
  print(x)

  # When working with a large data set or perhaps an infinite stream of data
  # in those situations we shouldn't store all those values in the memory (because that's very memrory inefficient)
  # in Situation like this is better to use a GENERATOR OBJECTS


  ## Creating a Generator Objects
values = (x * 2 for x in range(10))
for x in values:
  print(x)

  # size of generator: bytes of memory

size_of_generator_1000 = (x * 2 for x in range(1000))
print("gen: ", getsizeof(size_of_generator_1000))

size_of_generator_100000 = (x * 2 for x in range(100000))  # the size of generator object remains consisitent 
print("gen: ", getsizeof(size_of_generator_100000))

# size of the List - bytes of memory
size_of_list_100000 = [x * 2 for x in range(100000)]  
print("list: ", getsizeof(size_of_list_100000))

# We only can access the items of a Generator Object when we iterate over them
values = (x * 2 for x in range(100000))  # the size of generator object remains consisitent 
print(len(values))  # therefore ERROR!