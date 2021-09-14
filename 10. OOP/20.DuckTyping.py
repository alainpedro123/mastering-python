# 21. DUCK TYPING

class TextBox:
  def draw(self):
    print("TextBox")


class DropDownList:
  def draw(self):
    print("DropDownList")

# as long as the object we'll be looping through have the draw method pytho will be happy - Duck Typing
def draw(controls):  
  for control in controls:
    control.draw()     # this is still Polymorphism

#rendering the UI of an application
ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])  # 2. and that function will take care of rendering the entire form
