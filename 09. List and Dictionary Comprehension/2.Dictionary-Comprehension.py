### DICTIONARY COMPREHENSION - a collection of key values pair. We use it to map a key to a value

# 1. Creating a LIST with Comprehension expression
# a) Without Comprehension expression
list_values = []
for x in range(5):
  list_values.append(x*2)
print(list_values)

# b) With Comprehension expression
#[expression for item in items]
list_values_2 = [x * 2 for x in range(5)]
print(list_values_2)


# 2. Creating a SET with Comprehension expression

# b) With Comprehension expression
set_values_2 = {x * 2 for x in range(5)}
print(set_values_2)


## 3. Creating a DICTIONARY with Comprehension expression

# a) Without Comprehension Expression
dict_values = {}
for x in range(5):
  dict_values[x] = x * 2
print(dict_values)

# b) With Comprehension Expression
dict_values_2 = {x: x * 2 for x in range(5)}
print(dict_values_2)