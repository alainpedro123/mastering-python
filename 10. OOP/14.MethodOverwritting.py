# 14. METHOD OVERWRITING - overwriting or replacing a method in the parent class by using "super()"

class Animal(object):
  print("Animal Constructor")
  def __init__(self):
    self.age = 1

  def eat(self):
    print("eat")

class Mammal(Animal): 
  def __init__(self):
   print("Mammal Constructor") 
   self.weight = 2
   super().__init__()   # without this line we get an error: "Object has no attribute 'age' "

dog = Mammal()
print(dog.age)
print(dog.weight)     