from tkinter import *
import tkinter.messagebox

window=Tk()
# Tk() is a top-level widget which is used to create the main application window in which we will be building python to-do list applicatio
window.title('To-Do List App')
# The title() method is used to give a name to our application which is basically displayed at the top.

frame_task =Frame(window)
# Frame() method is basically a container widget within our main window and it is used to hold different widgets. It takes an argument that is our main window.
frame_task.pack()
# pack() method is a geometry manager which organizes the widget properly before placing it in the main window in a level order fashion until explicitly mentioned.


window.mainloop()
# The mainloop() method basically runs the Tkinter event loop, it runs and displays everything we have written in our code.