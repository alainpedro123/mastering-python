# EXAMPLE 1
myset = set();
myset.add(1)
myset.add(2)
myset.add(3)

mylist = [1,2,3,4,5]
myset2 = set(mylist)

# EXAMPLE 2
numbers = [1, 1, 2, 2, 4, 3]
print(numbers)

# converting the list into a set
set_uniques = set(numbers)
print(set_uniques)

# defining a new set
set_new = { 1, 4}
set_new.add(5)
set_new.remove(5)
len(set_new)
print(set_new)

# Sets shine in the Powerful Mathematical Operations that are supported by them
first = set(numbers)
second = {1, 2, 5, 6}

#union
print(first | second)

# intersection - the numbers that exist in both set 
print(first & second)

# difference
print(first - second)   # the elements that exist in the "first set" and don't exist in the "second set"
print(second - first)   # the elements that exist in the "second set" and don't exist in the "first set"
print(first ^ second)   # the elements that exist either in the first or second set but not both

# checking for the existance of 1
if 1 in first: 
  print("yes")