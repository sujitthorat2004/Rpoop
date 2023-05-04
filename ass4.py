#ass5:Write a program to display two labels with different colored background.

import tkinter as tk
#__init method is used too initialise attributes
#instance is an occurrence of a class that represents a specific object. When we create an instance of a class, we are creating a new object that has the properties and behaviors defined by that class.


#root window is first widget when tkinter appliaction was started .root window has a number of properties, such as a title, size, background color, and border.


root = tk.Tk()# Create a new instance of the main window,by using this we can create new main window object of Tk class ans we can use various methods in Tk class in 

root.title("colour labels and menubar")# Set the title of the main windowtkinter application

# Create a menu bar
menubar = tk.Menu(root)

#The tearoff option specifies whether or not the user can "tear off" the menu from the menu bar by dragging it with the mousetearoff=0 prevent it from dragging by mouse

# Create a file menu and add it to the menu bar
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
file_menu.add_command(label="Open")
file_menu.add_command(label="Save")
menubar.add_cascade(label="File", menu=file_menu)


#menubar.add_cascade is a method in the Menu class of the tkinter module that is used to add a hierarchical cascade of menus to a parent menu or menubar.

edit_menu = tk.Menu(menubar , tearoff = 0)
edit_menu.add_command(label="Add")
edit_menu.add_command(label="New")
menubar.add_cascade(label="Edit", menu=edit_menu)

# Configure the menu bar for the root window
root.config(menu=menubar)


# Create the first label widget with a red background and black text
label1 = tk.Label(root, text="Label 1", bg="Yellow", fg="red")

# Add the first label to the main window, and make it expand to fill any extra space
#tk.BOTH fillsthe widget both vertically and horizontally
label1.pack(fill=tk.BOTH, expand=True)

# Create the second label widget with a green background and black text
label2 = tk.Label(root, text="Label 2", bg="White", fg="Black")

# Add the second label to the main window, and make it expand to fill any extra space
label2.pack(fill=tk.BOTH, expand=True)

root.mainloop() # Start the main event loop to display the window




