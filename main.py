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

# Requirements
# - 2 dropdown menus. (select algo,speed)
# - 2 buttons. (generate random array,start sorting)
# - A canvas to draw array.

UI_frame = Frame(window, width=900, height=300, bg=BLUE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select Sorting Algorithms
l1 = Label(UI_frame, text='Algorithm: ', bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable = algo_name, values = algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed_name, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# Display
window.mainloop() # Infinite loop running application as long as window is not closed.

