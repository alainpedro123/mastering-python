# LIST COMPREHENSION - List comprehensions provide a brief way to create lists

# EXAMPLE 1 - Appending an element to the list
# 1a) with FOR LOOP
string = "hello"
mylist = []

for letter in string:
    mylist.append(letter)
print(mylist)

# 1b) with LIST COMPREHENSION
myList = [letter for letter in string]
print(mylist)


# EXAMPLE 2
# 2a) with element using NESTED LOOP
first = [2, 4, 6]
second = [1, 10, 1000]
result = []

for x in first:
    for y in second:
        result.append(x*y)
print(result)					# [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]


# 2b) with element using LIST COMPREHENSION
result = [x*y for x in first for y in second]
print(result)					# [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]


# EXAMPLE 3
# 3) Below operation with LIST COMPREHENSION
myList = [x for x in 'HelloWord']    # x is a temporary variable
# ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'd']
print(myList)

myList = [num for num in range(0, 11)]
print(myList)                        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


myList = [num**2 for num in range(0, 11)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(myList)


# EXAMPLE 4 - appending into the list only the even numbers
myList = [num**2 for num in range(0, 11) if num % 2 == 0]
print(myList)                       # [0, 4, 16, 36, 64, 100]


# EXAMPLE 5 - Temperature conversion from celsius to fahrenheit
celcius = [0, 10, 20, 34.5]

# a) With FOR-LOOP
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

# b) With LIST COMPREHENSION
fahrenheit = []

for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)


# EXAMPLE 6
items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]

# Sorting a list of tupples
prices = [item[1] for item in items]

# Filtering the number greater or equal to zero
filteredList = [item for item in items if item[1] >= 10]
