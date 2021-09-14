##### 8. LAMBDA FUCNTIONS
# Lambda expression - it's basically a simple, one line anonymous function that we can pass to other functions

#Sorting a list of tupples - second way
items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]

items.sort(key=lambda item:item[1])
print(items)