# 22. Data Classes - Dealing with classes with no behaviour, we can use a "named tuple" instead
from collections import namedtuple

# 1. Class with any methods, just data
class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __eq__(self, other):   # comparing 2 objects using magic methods
    return self.x == other.x and self.y == other.y
p1 = Point(1, 2)
p2 = Point(1, 2)

print(id(p1)) # address of the memory location where the object is stored


# 2. namedtupple - RECOMMENDED WAYS
# the namedtuple are immutable

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
# p1.x = 10 this throws an error, we can do the below instead
p1 = Point(x=10, y=2)
p2 = Point(1, 2)
print(p1 == p2)  # comparing two objects without using magic methods