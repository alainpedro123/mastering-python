# 10. PRIVATE METHODS 
# In Python don't really have the concept of private members. These private members are still accessible from the outside.
# thereforre using "self.__tags" is more of a convention to prevent accidental access of these private members
 
class TagCloud:
  def __init__(self):
    self.__tags = {} # private attribute -  by prefixing them with __

  def add(self, tag):
    self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

  def __getitem__(self, tag): 
    return self.__tags.get(tag.lower(), 0)

  def __setitem__(self, tag, count):
    self.__tags[tag.lower()] = count

  def __len__(self):
    return len(self.__tags)

  def __iter__(self):
    return iter(self.__tags)

cloud = TagCloud()
print(cloud.__dict__) # accessing a private attribute

# access the underlyning dictionary in this class
