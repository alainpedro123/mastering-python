# 13. OBJECT CLASS - is the parent class for all the classes in Python

# object is the parent class of Animal
class Animal(object):
  def __init__(self):
    self.age = 1

  def eat(self):
    print("eat")

# Animal: Parent class, Mammal: Child class
class Mammal(Animal):  # this is INHERITANCE 
   def walk(self):
    print("walk")

class Fish(Animal):
  def swim(self):
    print("swim")

# "Mamal" inherits from "Animal" which inherits from "object"
dog = Mammal()
print(isinstance(dog, Mammal))       
print(issubclass(Mammal, object))       
