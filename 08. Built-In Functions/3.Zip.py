##### 12. ZIP FUNCTION - Working with mutiple lists

list1 = [1, 2, 3]
list2 = [10, 20, 30]

# Combining these two above lists into a single list of tupples => [(1, 10), (2, 20), (3, 30)]
print(list(zip(list1, list2)))

print(list(zip("abc", list1, list2)))