import pandas as pd
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from contextlib import redirect_stdout
from io import StringIO
import time

from breed_chainV5 import *

# GUI function to calculate the breeding chain and display it
def gui_calculate_breed_chain():
    target_pal = target_pal_entry.get()
    inherited_pals = inherited_pal_entry.get().split(',')
    excluded_pals = excluded_pal_entry.get().split(',')  # Get excluded pals

    # Capture the output of the calculate_breed_chain function
    old_stdout = StringIO()
    with redirect_stdout(old_stdout):
        calculate_breed_chain(target_pal, inherited_pals, excluded_pals)  # Pass excluded pals
    output = old_stdout.getvalue()

    # Display the output in the ScrolledText widget
    output_text.delete("1.0", tk.END)  # Clear the current content
    output_text.insert(tk.END, output)  # Insert the new output

# Set up the GUI
root = tk.Tk()
root.title("Flip's Breeding Chain Calculator")

# Add a label and entry for the target pal
tk.Label(root, text="Target Pal:").pack()
target_pal_entry = tk.Entry(root)
target_pal_entry.pack()

# Add a label and entry for the inherited pals
tk.Label(root, text="Inherited Pals (comma-separated):").pack()
inherited_pal_entry = tk.Entry(root)
inherited_pal_entry.pack()

# Add a label and entry for the excluded pals
tk.Label(root, text="Excluded Pals (comma-separated):").pack()
excluded_pal_entry = tk.Entry(root)
excluded_pal_entry.pack()

# Add a button to trigger the calculation
calculate_button = tk.Button(root, text="Calculate Breeding Chain", command=gui_calculate_breed_chain)
calculate_button.pack()

# Add a ScrolledText widget to display the output
output_text = ScrolledText(root, height=20, width=80)
output_text.pack()

# Start the GUI loop
root.mainloop()
