# 1) DIFFERENT WAYS TO CREATE LISTS IN PYTHON
letters = ["a", "b", "c", "d"]
mix = ['string', 100, 23.2]
numbers = [1, 2, 3]
characters = list("Hello Word")		# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'd']
numbers = list(range(20))           # list of 20 elements from 0 to 19
zeros = [0] * 5                     # [0,0,0,0,0]
combined = zeros + letters          # [ 0, 0, 0, 0, 0, 'a', 'b', 'c']

matrix = [
	[0, 1], 
	[2, 3]
]

matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
]

mylist = [(1,2),(3,4),(5,6),(7,8)]
mylist = [(1,2,3),(4,5,6),(7,8,9)]

# 2) LIST INDEXING AND SLICING
myList = ['one', 'two', 'three', 'four']

myList[0]            # 'one'
myList[1:2]          # ['two', 'three']
myList[0] = 'Alain'  # ['Alain', 'one', 'two', 'three']
myList[0:3]
myList[:3]
myList[0:]
myList[:]

# 3) METHODS
append()
pop()
insert()
remove()
clear()
index()
count()
sort()
reverse()
copy()
extend()


# 4. LIST UNPACKING
numbers = [1, 2, 3]

# this is equal to to what we have below
first, second, third = numbers

# this is equivalent to what we have above
first = numbers[0]
second = numbers[1]
third = numbers[2]

numbers_2 = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *other = numbers_2
print(first)    # 1
print(second)   # 2
print(other)    # [3, 4, 4, 4, 4, 4]

numbers_3 = [1, 2, 3, 4, 4, 4, 4, 94]
first, *other, last = numbers_3
print(first, last)    # 1, 94
print(other)          # [2, 3, 4, 4, 4, 4]