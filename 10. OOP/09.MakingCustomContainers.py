# 9. MAKING CUSTOM CONTAINERS (DATA STRUCTURE) - CREATING OUR CLASS WITH THE METHODS: add, leng 
 
class TagCloud:
  def __init__(self):
    self.tags = {}

  def add(self, tag):
    # checking if we this tag exists in the dictionary, if not we're gonna set its value to 1, otherwise we're going to increment it by 1
    #self.tags[] = self.tags.get(tag, 0) + 1 # get( tag - get an item by its key, 0- supply a default value if we don't have this value)
    self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1 # adding the "lower()" method  so that python == Python 
  
  def __getitem__(self, tag): # read the count of tag 
    return self.tags.get(tag.lower(), 0)  # tag - with this word exists returns it, otherwise 0 -> returns 0 

                      # key, value
  def __setitem__(self, tag, count): # setting a number for a given item:  cloud["python"] = 10
    self.tags[tag.lower()] = count

  def __len__(self):
    return len(self.tags)

  def __iter__(self):
    return iter(self.tags) # iter() - it returns an iterator object which give us one item at a time in for loop

cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
print(cloud.tags)

cloud["python"] = 10  # setting the key "10"
print(cloud.tags)

len(cloud)
for tag in cloud:     # iterating over the container
  print(tag)


# The get() method returns the value for the given key, if present in the dictionary. If not, then it will return None (if get() is used with only one argument).