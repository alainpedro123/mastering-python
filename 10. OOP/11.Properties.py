# 11. PROPERTIES 
# Having control over an attribute in a class. For example: ensure that our product din't have negative prices
# Property is an object that sists in front of an attribute and allows us to get or set the value of an attribute

# First way 
class Product:
  def __init__(self, price):
    self.set_price(price)

  def get_price(self):
    return self.__price

  def set_price(self, value):
    if value < 0:
      raise ValueError("Price cannot be negative")
    self.__price = value
  
  # defining a property
  price = property(get_price, set_price) #passing a reference of these 2 functions

product = Product(10)
print(product.price)



# Second way
class Product:
  def __init__(self, price):
    self.price = price
  
  # Creating a PROPERTY with Decorators
  # the code below will automaticly create a property object called "price"
  @property
  def price(self):
    return self.__price

  @price.setter
  def price(self, value):
    if value < 0:
      raise ValueError("Price cannot be negative")
    self.__price = value

product = Product(-10)
print(product.price)
