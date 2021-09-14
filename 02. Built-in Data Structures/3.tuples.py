# TUPLES – are very similar to lists. However they have one key difference „immutability”. it's a read only list, no manipulation data
# Tuples and Lists share the same built-in methods

t1 = (1,2,3)
t2 = (1, 'two', 3.1)
t3 = ('a', 'b', 'c')


# EXAMPLES

point = 1   # this is an integer
point = 1,  # this a Tuple
point = (1, 2)   # it's the same as point = 1,2

point = (1, 2) + (3, 4)   # (1, 2, 3, 4)
print(point)

point = (1, 2) * 3    # (1, 2, 1, 2, 1, 2)
print(point)

# converting a list into a tupple
point = tuple([1, 2]) 
print(point)

# converting a string into a tupple
point = tuple("Hello World") 
print(point)

# accesing items
point = (1, 2, 3)
print(point[0])
print(point[0:2])

#unpacking the tupples
x, y, z = point
print(point)

if 10 in point:
  print("it exists")
else:
  print("10 is not in this tuple")


# We can use Tuple when for example dealing with a sequence of objects, and you wanna make sure that you won't either accidentally modify this sequence, add a new object or removing an existing one... to prevent this accidental errors we use tuples