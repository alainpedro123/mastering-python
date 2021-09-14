# 3. CONSTRUCTOR - a special method that is called when creating a new point object
# The methods that we define in the class should have at least one parameter which by convention we call "self"
# and "self" references the current point object we're working with

class Point:
  def __init__(self, x, y):   ## Constructor - a magic method
    self.x = x
    self.y = y

  def draw(self):
    print(f"Point ({self.x}, {self.y})")

point = Point(1, 2)
print(point.x)
point.draw()  # when calling methods in an object, we never have to supply a value for this parameter, python interpreter does that for us
