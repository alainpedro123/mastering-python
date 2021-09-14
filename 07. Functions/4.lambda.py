##### 8. LAMBDA FUCNTIONS
# Lambda expression - it's basically a simple, one line anonymous function that we can pass to other fucntions

#Sorting a list of tupples 
items = [
    ("Product1", 10),
    ("Product1", 9),
    ("Product1", 12),
]

# A) Using Lambda
items.sort(key=lambda item:item[1])
print(items)

# B) Using lambda + map() function
prices = list(map(lambda item: item[1], items))   

# C) Using list comprehension
prices = [item[1] for item in items] 
