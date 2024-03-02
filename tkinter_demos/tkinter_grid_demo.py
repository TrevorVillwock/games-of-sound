# source: https://www.geeksforgeeks.org/python-grid-method-in-tkinter/
# import tkinter module

from tkinter import *
from tkinter.ttk import *

# create main tkinter window
root = Tk()

l1 = Label(root, text = "Label 1")
l2 = Label(root, text = "Label 2")

l1.grid(row = 0, column = 0, sticky = W, pady = 2)
l2.grid(row = 1, column = 0, sticky = W, pady = 2)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row = 0, column = 1, pady = 2)
e2.grid(row = 1, column = 1, pady = 2)

c1 = Checkbutton(root, text = "Check")
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2)

img = PhotoImage(file = "./piano.png")
img1 = img.subsample(2, 2)

Label(root, image = img1).grid(row = 0, column = 2, columnspan = 2, rowspan = 2, padx = 5, pady = 5)

b1 = Button(root, text = "Button 1")
b2 = Button(root, text = "Button 2")

b1.grid(row = 2, column = 2, sticky = E)
b2.grid(row = 2, column = 3, sticky = E)

root.mainloop()