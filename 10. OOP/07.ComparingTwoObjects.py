# 7. COMPARING TWO OBJECTS - with magic methods
 
class Point:
  def __init__(self, x, y):   
    self.x = x    
    self.y = y   
    
  def __eq__(self, other):      # Equal
    return self.x == other.x and self.y == other.y

  def __gt__(self, other):      # Greater than
    return self.x > other.x and self.y > other.y
  
point = Point(1, 2)
other = Point(1, 2)
print(point == other)

point = Point(10, 20)
other = Point(1, 2)
print(point > other)
print(point < other)