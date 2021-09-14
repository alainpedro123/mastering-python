# 16. MULTIPLE INHERITANCE - which should be avoided!!

class Employee:
  def greet(self):
    print("Employee greet")

class Person:
  def greet(self):
    print("Person greet")

class Manager(Person, Employee):    # this is a multiple inheritance
  pass

manager = Manager()
manager.greet()

## A good example of Multiple Inheritance
class Flyer:
  def fly(self):
    pass

class Swimmer:
  def swim(self):
    pass

class FlyingFish(Flyer, Swimmer):    # this is a multiple inheritance
  pass