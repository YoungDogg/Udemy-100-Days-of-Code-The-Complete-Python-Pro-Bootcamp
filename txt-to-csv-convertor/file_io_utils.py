import os
import csv
from tkinter import messagebox
import locale

def write_to_csv(data, file_path):
    if os.path.exists(file_path):
        system_lang = locale.getdefaultlocale()[0]
        if system_lang.startswith('en'):
            msg = "File already exists. Do you want to replace it?"
        else:
            msg = "File already exists. Do you want to replace it?"  # You can translate this into other languages as needed.

        response = messagebox.askyesno("Confirmation", msg)
        if not response:
            return

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['ID', 'Password', 'Code'])
        for row in data:
            writer.writerow(row)
            
# New function
def read_txt_file(file_path):
    with open(file_path, 'r') as f:
        return f.readlines()