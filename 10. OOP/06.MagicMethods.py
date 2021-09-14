# 6. MAGIC METHODS
# MAGIC METHODS - are called automaticly by Python Interpreter depending on how we use our Object and Class  

class Point:
  def __init__(self, x, y):   # 1. this is a "magic method"
    self.x = x    
    self.y = y   

  def __str__(self):   # 3. defining a new "magic method" - getting a string representation of this point object
    return f"({self.x}, {self.y})"

  def draw(self):             
    print(f"Point ({self.x}, {self.y})")

# 2. this is a magic method is automaticly called by Python Interpreter when we create a new point object 
point = Point(1, 2)
print(point)
print(str(point))