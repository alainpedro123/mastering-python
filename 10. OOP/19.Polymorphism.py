# 19. POLYMORPHISM

from abc import ABC, abstractmethod

class UIControl(ABC):
  @abstractmethod
  def draw(self):
    pass

class TextBox(UIControl):
  def draw(self):
    print("TextBox")


class DropDownList(UIControl):
  def draw(self):
    print("DropDownList")

# 1. taking a list of all the UI components and pass it a function like draw  
def draw(controls):  #it takes a UI control  object
  for control in controls:
    control.draw()     # calls the draw method of each control object (component). This is a polymorphism function 
# POLYMORPHISM - the above function

#rendering the UI of an application
ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])  # 2. and that function will take care of rendering the entire form