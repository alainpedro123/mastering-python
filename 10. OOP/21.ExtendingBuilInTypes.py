# 21. Extending Built-in Types
# Using Inheritance with BuiltIn Class

# creating a Class Text that inherits from the Str(string) Class
class Text(str):
  def duplicate(self):
    return self + self

# creating a TrackableList that inherits from the List Class
class TrackableList(list):
  def append(self, object):
    print("Append called")
    super().append(object)  # extending the append method of the list class


text = Text("Python")
print(text.lower())
print(text.duplicate())

list = TrackableList()
list.append("1")