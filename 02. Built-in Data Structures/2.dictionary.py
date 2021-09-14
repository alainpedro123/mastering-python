dictionary = {
  'key1': 'value1',
  'key2': 'value2'
}

point = dict(x=1, y=2)  # point = {"x": 1, "y": 2}


fruits = {
  'apple': 2.99,
  'orange': 3.40,
  'peach': 3.50
}

fruits['apple']   # 2.99

# Dictionary can have as value list, and dictionary as its value

dictionary2 = {
  'k1': 123,
  'k2': [1, 2, 3],
  'k3': {'insideKey': 100}
}

dictionary2['k1'][2]                # 2
dictionary2['k3']['insideKey']      # 100

dictionary3 = { 'key1': ['a', 'b', 'c', 'd']}
dictionary3['key1'][2].upper()


#METHODS

#getting the keys of the dictionary
dictionary.keys()

#getting the values of the dictionary
dictionary.values()

#
dictionary.items()


# getting the value associated with the key x
print(point["x"])

# changing the value of x to 10
point["x"] = 10
print(point)

# adding a new key
point["z"] = 20
print(point)

# checking for the existance of the key
if "a" in point:
  print(point["a"])
print(point.get("a", 0)) # else returns 0 by default

# deleting a number
del point["x"]
print(point)

#Iterate over abs dictionary - first way

for key in point:
  print(key, point[key])

#Iterate over abs dictionary - Second way - we get a tupple in each iteration, so we can unpack those
for key, value in point.items():
  print(key, value)