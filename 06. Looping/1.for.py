# Example 1 - Print the numbers of the list
list = [2, 4, 6, 8]

for num in list:
    print(num)



# Example 2 - Print the indexes - using "range" function
list = [2, 4, 6, 8]

for num in range(len(list)):
  print(num)



# Example 3 - Print the values and indexes
values = ['a', 'b', 'c']

for index in range(len(values)):
    value = values[index]
    print(index, value)



# Example 4 - Print the values and indexes II - using "enumerate" function
values = ['a', 'b', 'c']

for index, value in enumerate(values):
    print(index, value)



# Example 5 - Print the values and indexes of the string "helloo"
# a)
for index, value in enumerate('helloo'):
  print(f'{index}, {value}')

# b)
string = "abcde"

for index, letter in enumerate(string):
	print('At index {} the letter is {}'.format(index, letter))



# Example 6 - Print the numbers from 0 to 5
for num in range(0, 6):
    print(num)

# Alternatively, you can do like this
for num in range(6):
    print(num)



# Example 7 - Print the numbers from 2 to 29, increment the sequence with 3 (the default is 1):
# result: 2, 5, 8, 11, 14, 17, 20, 23, 26, 29
for x in range(2, 30, 3):
  print(x)



# Example 8 - Print all the pairs - use "nested loop"
# a) result: (a,a); (a,b); (a,c); (b,a); (b,b); (b,c); (c,a); (c,b); (c,c) ....

array = ['a', 'b', 'c', 'd', 'e']

n = len(array)
for i in range(0, n):
    for j in range(0, n):
        print(array[i] + "," + array[j])


# b) result: # (0, 0); (0, 1); (0, 2); (1, 0); (1, 1); (1, 2); (2, 0); (2, 1); (2, 2); (3, 0); (3, 1); (3, 2); (4, 0); (4, 1); (4, 2); 
for x in range(5):  # The Outer Loop
    for y in range(3):  # The Inner Loop
        print(f"({x}, {y})")



# Example 9 - using nested loops, print each adjective for every fruit:
# result: (red apple); (red banana); (red cherry); (big apple); (big banana); (big cherry); (tasty apple); (tasty banana); (tasty cherry); 
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



# Example 10 - Looping Through a String "banana"
# a) result: banana
for char in "banana":
    print(char)

# b) result: Sammy
string = "Sammy"

for letter in string:
	print(letter)



# Example 11 - Using "break", "continue" and "pass" keywords
# a) BREAK
# 1 - Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]

for x in fruits:
  print(x)
  if x == "banana":
    break

# 2 - breaks out if it encounters the letter "a".
for letter in string:
	if letter == 'a':
		break
	print(letter)


# b) CONTINUE
# 1 - Do not print banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


# 2 - If you find the letter 'a' please ignore it and continue.
for letter in string:
	if letter == 'a':
		continue
	print(letter)


# c) PASS
# 1 - "for" loops cannot be empty, but if for some reason you must have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

# 2 - "pass" does nothing at all
x = [1, 2, 3]
for item in x:
	# comment
	pass
print('end of my code')
 


# Example 12 - Print the pair of numbers and letters
# zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
l1 = [1,2,3]
l2 = ['a','b','c']
for item in zip(l1,l2):
	print(item)


# Example 13 - Loop through 3 arrays simultaneously - using "zip" function
first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]

for one, two, three in zip(first, second, third):
    print(one, two, three)



# Example 14 - Combining "zip" and "enumerate" by using nested argument unpacking:
first = ["a", "b", "c"]
second = ["d", "e", "f"]
third = ["g", "h", "i"]

for count, (one, two, three) in enumerate(zip(first, second, third)):
    print(count, one, two, three)

#### Result:
# 0 a d g
# 1 b e h
# 2 c f i 



# Example 15 - print the below:
# (1, 'a', 100)
# (2, 'b', 200)
# (3, 'c', 300)

l1 = [1,2,3]
l2 = ['a','b','c']
l3 = [100, 200, 300]
for item in zip(l1,l2,l3):
	print(item)



# Example 16- Put the pin to unlock your phone - you have only 3 attempts
pin = 1234

for attempt in range(3):  # setting 3 attempts
    print("Enter the pin")
    if pin == 1234:
        print("Successful")
        break
# If you fail 3 times 
print("Sorry, your phone has been blocked")



# Example 17 - Loop through a dictionary - By default is set iteration through the keys
dictionary = {
  'k1': 1,
  'k2': 2,
  'k3': 3
}

# print the keys
for key in dictionary:
	print(key)

# print the values
for value in dictionary.items():
	print(value)

# print both keys and values
for key,value in dictionary.items():
	print(value)



# Example 18 - Loop through a tuple
tup = (1,2,3)
for num in tup:
	print(num)



# Example 19 - Loop through a list of tuple
mylist = [(1,2),(3,4),(5,6),(7,8)]

for num in mylist:
	print(num)

for (a,b) in mylist:
	print(a)

for (a,b) in mylist:
	print(b)

for (a,b) in mylist:
	print(a)
	print(b)


# Example 20 - Loop through a list of tuple
mylist = [(1,2,3),(4,5,6),(7,8,9)]

for item in mylist:
	print(item)



  
# "enumerate" - More examples
# https://realpython.com/python-enumerate/

# LOOPING WITH INDEXES
# https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
