# 1) COMPARISON OPERATORS
a == b		# False
a != b		# True
a > b		# False
a < b		# True
a >= b		# False
a <= b		# True

# 2) CHAINED COMPARISON OPERATIONS - and, or, not
1 < 2 > 3				# False

1 < 2 and 2 > 3			# False
1 < 2 and 2 < 3			# True
'h'=='h' and 2 == 2		# True

1 == 1 or 2 == 2		# True
100 == 1 or 2 == 2		# True
100 == 1 or 2 == 1		# False

not 1 == 1				# False
not 1 > 2				# True

# 3) IN operator
'x' in ['x','y','z']  			# True
'a' in 'a world'				# True
'mikey' in {'mikey': 353}		# True

d = {'mikey': 353}
354 in d.keys()					# False

# 4) LOGICAL OPERATORS
# a) Example
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

# b) Example
age = 22
if 18 <= age < 65:  # if age >= 18 and age < 65:
    print("Eligible")

# This is called Short-Circuit. This expression will always be true because at least one of the variable is false
if high_income or good_credit and not student:
    print("Eligible")


# 5) UNPACKING OPERATOR
# We use Unpacking Operator to take out invidual values in any iterable

numbers = [1, 2, 3]
print(numbers)

# Unpacking - printing the individual numebrs of the list 
print(*numbers)

values = list(range(5))
print(values)

# Unpacking list and string
values = [*range(5), *"Hello"]
print(values)

# Combining multiple lists
first = [1, 2]
second = [3, 4]
values_2 = [*first, "a", *second, *"Hello"]
print(values_2)

# Unpacking Dictionary
dic1 = {"x": 1}
dic2 = {"x": 10, "y": 2}
combined = { **dic1, **dic2, "z":1 }
print(combined)
