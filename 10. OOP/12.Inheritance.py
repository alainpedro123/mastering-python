# 12. INHERITANCE

# a) Without Inheritance
class Mammal:
  def eat(self):
    print("eat")

class Fish:
  def eat(self):
    print("eat")
  
  def swim(self):
    print("swim")



# b) With Inheritance
class Animal:
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

dog = Mammal()
dog.eat()          # inheriting the method "eat"
print(dog.age)     # inheriting the attribute "age"