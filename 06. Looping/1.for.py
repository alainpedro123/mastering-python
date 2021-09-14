string = "Sammy"

# EXAMPLE 1
for letter in string:
	print(letter)

# EXAMPLE 2
# FOR loop + break, continue, pass - add additional functionality for various cases.
# a) BREAK: breaks out the current closest enclosing loop.
for letter in string:
	if letter == 'a':
		break
	print(letter)


# b) PASS - does nothing at all. - ITERATION THROUGH A LIST
x = [1, 2, 3]
for item in x:
	# comment
	pass
print('end of my code')


# c) CONTINUE: goes to the top of the closest enclosing loop.
for letter in string:
	if letter == 'a':
		continue
	print(letter)


# EXAMPLE 3 - ITERATION THROUGH A TUPLE
tup = (1,2,3)
for num in tup:
	print(num)

# EXAMPLE 4 - ZIP() METHODS: This function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
l1 = [1,2,3]
l2 = ['a','b','c']
for item in zip(l1,l2):
	print(item)

# EXAMPLE 5
l3 = [100, 200, 300]
for item in zip(l1,l2,l3):
	print(item)

# EXAMPLE 6 - ITERATION THROUGH A LIST OF TUPLE
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

# EXAMPLE 7
mylist = [(1,2,3),(4,5,6),(7,8,9)]

for item in mylist:
	print(item)


# EXAMPLE 8 - ITERATION THROUGH A DICTIONARY - BY DEFAULT ITERATION THROUGH THE KEYS IS SET
dictionary = {
  'k1': 1,
  'k2': 2,
  'k3': 3
}

for key in dictionary:
	print(key)

for item in dictionary.items():
	print(item)

for key,value in dictionary.items():
	print(value)


# EXAMPLE 9 - ITERATION THROUGH A STRING

string = "abcde"

index_count = 0
for letter in string:   
	print('At index {} the letter is {}'.format(index_count, letter))
  index_count += 1


index_count = 0
for letter in string:   
	print(string[index_count])
  index_count += 1


# EXAMPLE 10 - enumerate()
 # It allows us to loop over something and have an automatic counter.
 # Tnumerate also accepts an optional argument which makes it even more useful.
 # The optional argument allows us to tell enumerate from where to start the index

# a) EXAMPLE
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)   # printing the indexes and values - A tuple

# b) EXAMPLE
 word = 'abcde'
 for item in enumerate(word):
 	print(item)

# c) EXAMPLE
for index, char in enumerate(word):
 	print(index)
 	print(letter)
 	print('\n')


# EXAMPLE 11 - FOR + range() function

# print all numbers from 0 to 9
for num in range(10):   
	print(num)

# print all numbers from 3 to 9
for num in range(3,10):   
	print(num)

# print all numbers from 0 to 9. 2 is the step sizer.
for num in range(0,10,2):   
	print(num)


# EXAMPLE 12  - FOR... ELSE
successful = True
for number in range(3):  # from o to 3
    print("Attempt")
    if successful:
        print("Successful")
        break

# 3 attempts but it didn't work
successful = False
for number in range(3):  # from o to 3
    print("Attempt")
    if successful:
        print("Successful")
        break
else:  # else with be exectuted only if the loop completes without termination
    print("attempted 3 times and failed")


# the loop won't be executed for this particular case
successful = True
for number in range(3):  # from o to 3
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("attempted 3 times and failed")


# EXAMPLE 13 - NESTED LOOP

for x in range(5):  # The Outer Loop
    for y in range(3):  # The Inner Loop
        print(f"({x}, {y})")



# LOOPING WITH INDEXES
https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/
