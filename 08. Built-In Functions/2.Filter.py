def check_even(num):
	return  % 2 == 0

numbers = [1,2,3,4,5,6]

# EXMAPLE 1 
for n in filter(check_even, numbers):	# 2,4,6
	print(n)

# EXAMPLE 2
list(filter(check_even, numbers))		# [2,4,6]


# EXAMPLE 3
# Filtering the below list and getting only the prices greater than or equal to $10

items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]
#lambda function takes an item and returns a boolean value tha determine if this item matches the criteria or not
filteredList = list(filter(lambda item: item[1] >=10, items)) 
print(filteredList)