# 5. CLASS VS INSTANCE METHODS

class Point:
  def __init__(self, x, y):   # this is an instance method
    self.x = x    
    self.y = y   

  # 1. defining a Class Method
  @classmethod # this is called a decorator and it's a way to extend the behavior of a method 
  def zero(cls):
    return cls(0, 0)

  def draw(self):             # this is an instance method
    print(f"Point ({self.x}, {self.y})")


# 2. calling the Class Method
point = Point.zero() # this is a class method. It's equivant to -> point = Point(0, 0)
point.draw() 