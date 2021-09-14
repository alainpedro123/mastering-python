# 2. CREATING CLASSES

class Point:
  def draw(self):  # self is a reference to the current point object
    print("draw")

# creating an object
point = Point()
print(point.draw())

# checking if an object is an instance of a given class
print(isinstance(point, Point))