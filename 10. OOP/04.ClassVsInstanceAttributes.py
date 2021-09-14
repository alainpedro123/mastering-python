# 4. CLASS VS INSTANCE ATTRIBUTES
# Instance Attributes - at Instance Attributes - attributes that belong to point instances or point  object
# Class Attributes - attributes that we define at class level and they are the same across all instances of teh class
# Examples: All humans have 2 eyes and 2 ears, these attributes that we define at class level and they are shared acrross all instances of a class

class Point:
  default_color = "red"  # this is a class attribue

  def __init__(self, x, y):  
    self.x = x    # this is an instance attribute
    self.y = y    # this is an instance attribute

  def draw(self):
    print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
point.z = 10  # creating attributes after creating a point object
point.draw() 
print(point.default_color)

# creating another point object (instance attributes)
another_point = Point(3,4)
another_point.draw()
