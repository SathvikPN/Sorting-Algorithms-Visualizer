# Main Executable file to run the visualizer project.
# Import all packages and modules in this file.
# Setup basic Graphical User Interface


# ---------------------------------------------------------
# From tkinter import all
from tkinter import *

# To configure tkinter widgets with style
from tkinter import ttk 

# To create random sequence
import random

# Import colors for project
from colors import *


# ---------------------------------------------------------
# Create a basic window. (Root window)
window = Tk() # assign window as window object name
window.title("Sorting Algorithms Visualizer")
window.maxsize(1200,600)
window.config(bg = WHITE)
window.geometry('800x400')

# ---------------------------------------------------------
# VARIABLES
# StringVar(): class to monitor changes to tkinter variables. 
# # (eg: via buttons)

algo_name = StringVar() 
algo_list = ["Bubble-sort","Merge-sort"]

speed_name = StringVar()
speed_list = ['Fast','Medium','Slow']

# Empty list fills with random values
# when we generate new random array to feed the sorter
data = []

# ---------------------------------------------------------
# FUNCTIONS

# visualize randomized sequence feed as vertical bars
def drawData(data,colorArray):
  pass

# generate array of random values to feed sorter
def generate():
  pass

# set sorting speed
def set_speed():
  pass

# This will Trigger the selected algorithm and start sorting
def sort():
  pass

# ---------------------------------------------------------
### USER INTERFACE HERE ###


# Display
window.mainloop() # Infinite loop running application as long as window is not closed.

