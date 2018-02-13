# Problem Set 7, Part IV
# Name: Kim, Matthew


# Don't change/remove this line please.
from Tkinter import *

# Don't change this function please.
def draw_triangle(p1, p2, p3):
   """Draw a triangle whose corners are given by tuples p1, p2, and p3."""
   window.create_polygon(*(p1+p2+p3), fill='red3')

# Don't change this function please.
def sierpinski(n):
   p1 = (100, 450)
   p2 = (300, 103.6)
   p3 = (500, 450)
   sierpinski_helper(n, p1, p2, p3)
   return None

# Complete the following function defintion. Feel free to define any other
# function that might help you simplify your code.
def sierpinski_helper(n, p1, p2, p3):
   # this function has to be recursive.
   # the rest of this function.
   if n == 1:
      return draw_triangle(p1,p2,p3)
   p12 = (((p1[0] +p2[0])/2), (p1[1] + p2[1])/2)
   p13 = (((p1[0] +p3[0])/2), (p1[1] + p3[1])/2)
   p23 = (((p2[0] +p3[0])/2), (p2[1] + p3[1])/2)  
   return sierpinski_helper((n-1), p1, p12, p13), sierpinski_helper((n-1),p12, p2,p23), sierpinski_helper((n-1),p13,p23,p3)

# Please don't change the following two lines.
window = Canvas(Tk(), width=600, height=600)
window.pack()

# Change the argument in the following function call to try different examples
# (inputs). For example, try sierpinski(4). Try sierpinski(6)
sierpinski(1)

# Please keep the following line at the end of your code.
mainloop()
