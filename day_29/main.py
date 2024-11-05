import tkinter as tk
import pandas as pd
import os.path

class Main:
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # if saved, delete entries except Email
    # required: button action, pandas saving, delete entries
    # button action
    def set_add_btn_command(self, callback):
        self.add_btn_command = callback

    # pandas saving
    def init_save_file(self):
        def init_save_file(self):
            if not os.path.exists(self.__file_name):
                # Create initial DataFrame
                self.__data_dict = {
                    'Website': ['somewebsite', 'apple'],
                    'Email/Username': ['alefe@gmail.com', '000@msx.com'],
                    'Password': ['woeijfeif', '383fjfj']
                }
                self.__data = pd.DataFrame(self.__data_dict)
                # Generate the 'Formatted' column
                self.__data['Formatted'] = self.__data[['Website', 'Email/Username', 'Password']].astype(str).apply(
                    lambda x: ' | '.join(x), axis=1)
                # Save to file
                self.__data.to_csv(self.__file_name, index=False, header=False)
            else:
                # Load existing data and add 'Formatted' if missing
                self.__data = pd.read_csv(self.__file_name, header=None,
                                          names=['Website', 'Email/Username', 'Password'])
                if 'Formatted' not in self.__data.columns:
                    self.__data['Formatted'] = self.__data[['Website', 'Email/Username', 'Password']].astype(str).apply(
                        lambda x: ' | '.join(x), axis=1)

        # Save only the 'Formatted' column
        def save_data2file(self):
            self.__data['Formatted'].to_csv(self.__file_name, index=False, header=False)
            print(self.__data)

    def save_data2file(self):
        self.__data['Formatted'].to_csv(self.__file_name, index=False, header=False)

    # ---------------------------- UI SETUP ------------------------------- #
    def __init__(self):
        self.__data_dict = None
        self.__data = None
        self.__file_name = 'data.txt'

        # Initialize the main window
        root = tk.Tk()
        root.title("Password Manager")

        # Configure the grid layout
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)
        root.grid_columnconfigure(2, weight=1)

        # Load the logo image (Make sure it's a .png or .gif file)
        logo_path = "logo.png"  # Replace with your image path
        logo_image = tk.PhotoImage(file=logo_path)

        # Display the logo image in the top row, centered
        logo_label = tk.Label(root, image=logo_image)
        logo_label.grid(row=0, column=1, pady=(20, 20))

        # Website label and entry
        website_label = tk.Label(root, text="Website:")
        website_label.grid(row=1, column=0, padx=(20, 10), sticky="e")
        website_entry = tk.Entry(root, width=35)
        website_entry.focus()
        website_entry.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=(5, 5), sticky="w")

        # Email/Username label and entry
        email_label = tk.Label(root, text="Email/Username:")
        email_label.grid(row=2, column=0, padx=(20, 10), sticky="e")
        email_entry = tk.Entry(root, width=35)
        email_entry.insert(0, "dummy@email.com")
        email_entry.grid(row=2, column=1, columnspan=2, padx=(0, 20), pady=(5, 5), sticky="w")

        # Password label, entry, and generate button
        password_label = tk.Label(root, text="Password:")
        password_label.grid(row=3, column=0, padx=(20, 10), sticky="e")

        # Frame to hold password entry and button together
        password_frame = tk.Frame(root)
        password_frame.grid(row=3, column=1, columnspan=2, sticky="w")

        # Password entry inside the frame
        password_entry = tk.Entry(password_frame, width=20)
        password_entry.grid(row=0, column=0, padx=(0, 5))

        # Generate button inside the frame, right next to the entry
        generate_button = tk.Button(password_frame, text="Generate Password")
        generate_button.grid(row=0, column=1)

        # Add button
        self.add_btn_command = None
        add_button = tk.Button(root, text="Add", width=36, command=self.add_btn_command)
        add_button.grid(row=4, column=1, columnspan=2, pady=(10, 20), padx=(0, 20), sticky="w")

        # Run the application
        root.mainloop()

    @property
    def data_dict(self):
        return self.__data_dict

    @data_dict.setter
    def data_dict(self, val):
        self.__data.loc[0,'Website'] = val

    def add_btn_command(self):
        if self.add_btn_command:
            self.add_btn_command()


if __name__ == '__main__':
    m = Main()
    m.init_save_file()
    m.data_dict = 'Microsoft'
    m.save_data2file()
