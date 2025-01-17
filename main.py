import tkinter as tk
from Gui import CrapsGameGUI

# Create the main window
root = tk.Tk()

# Create the game GUI
app = CrapsGameGUI(root)

# Start the GUI event loop
root.mainloop()
