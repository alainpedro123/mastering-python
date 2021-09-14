# 15. MULTI LEVEL INHERITANCE - which should be avoided!!

class Animal:
  def eat(self):
    print("eat")

class Bird(Animal): 
  def fly(self):
   print("fly") 

class Chicken(Bird):    # this is a multi level inheritance: Animal - Bird - Chicken
  pass