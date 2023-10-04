import tkinter as tk
from tkinter import filedialog

def select_txt_files():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilenames(title="Select one or more TXT files", filetypes=[("TXT files", "*.txt")])


