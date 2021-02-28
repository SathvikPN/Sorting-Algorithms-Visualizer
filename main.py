# Main Executable file to run the visualizer project.
# Import all packages and modules in this file.
# Setup basic Graphical User Interface


# From tkinter import all
from tkinter import *

# To configure tkinter widgets with style
from tkinter import ttk 

# To create random sequence
import random

# Import colors for project
from colors import *

# Create a basic window. (Root window)
window = Tk() # assign window as window object name
window.title("Sorting Algorithms Visualizer")
window.maxsize(1200,600)
window.config(bg = WHITE)
window.geometry('650x350')

# Display
window.mainloop()
# Infinite loop running application as long as window is not closed.
