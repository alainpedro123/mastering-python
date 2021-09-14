# EXAMPLE 1
def square(num):
	return num**2

numbers = [1,2,3,4,5]

for item in map(square, numbers):
	print(item)

# EXAMPLE 2
list(map(square, numbers))   # [1,4,9,16,25]

# EXAMPLE 3
def splicer(string):
	if len(string) % 2 == 0
		return 'EVEN'
	else: 
		return string[0]

names = ['Andy', 'Eve', 'Sally']
list(map(splicer, names))		# ['EVEN', 'E', 'S']


# EXAMPLE 4

items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]

## Transforming the list "items" into a list of numbers (price)  => [10, 9, 12]
# a) Using FOR loop
prices = []
for item in items:
  prices.append(item[1])

print(prices)


# b) Using MAP - It returns 3 separates numbers: 10, 9 and 12
prices_x = map(lambda item: item[1], items) 
for item in prices_x:
  print(item)

# c) Using MAP - It returns a list: [10, 9, 12]
prices_y = list(map(lambda item: item[1], items))
print(prices_y)