import tkinter as tk
from tkinter import messagebox


class UI:
    def __init__(self):
        self.logo_image = None
        self.__password_entry = None
        self.__website_entry = None
        self.__email_entry = None
        self.__add_data_btn_command = None
        self.__generate_pswd_btn_command = None
        self.__search_website_btn_command = None
        self.__root = None
        self.__clipboard = None

    def setup_ui(self):
        # Initialize the main window
        self.__root = tk.Tk()
        self.__root.title("Password Manager")

        # Configure the grid layout
        self.__root.grid_columnconfigure(0, weight=1)
        self.__root.grid_columnconfigure(1, weight=1)
        self.__root.grid_columnconfigure(2, weight=1)

        # Load the logo image (Make sure it's a .png or .gif file)
        logo_path = "../day_29/logo.png"  # Replace with your image path
        self.logo_image = tk.PhotoImage(file=logo_path)

        # Display the logo image in the top row, centered
        logo_label = tk.Label(self.__root, image=self.logo_image)
        logo_label.grid(row=0, column=0, columnspan=3, pady=(20, 20), sticky="n")

        # Website label and entry
        website_label = tk.Label(self.__root, text="Website:")
        website_label.grid(row=1, column=0, padx=(20, 10), sticky="e")
        self.__website_entry = tk.Entry(self.__root, width=35)
        self.__website_entry.focus()
        self.__website_entry.grid(row=1, column=1, padx=(0, 5), pady=(5, 5), sticky="w")

        search_button = tk.Button(self.__root, text="Search", command=self.__search_website_btn_command)
        search_button.grid(row=1, column=2, padx=(5, 20), pady=(5, 5), sticky="w")

        # Email/Username label and entry
        email_label = tk.Label(self.__root, text="Email/Username:")
        email_label.grid(row=2, column=0, padx=(20, 10), sticky="e")
        self.__email_entry = tk.Entry(self.__root, width=35)
        self.__email_entry.insert(0, "dummy@email.com")
        self.__email_entry.grid(row=2, column=1, columnspan=2, padx=(0, 20), pady=(5, 5), sticky="w")

        # Password label, entry, and generate button
        password_label = tk.Label(self.__root, text="Password:")
        password_label.grid(row=3, column=0, padx=(20, 10), sticky="e")

        # Frame to hold password entry and button together
        password_frame = tk.Frame(self.__root)
        password_frame.grid(row=3, column=1, columnspan=2, sticky="w")

        # Password entry inside the frame
        self.__password_entry = tk.Entry(password_frame, width=20)
        self.__password_entry.grid(row=0, column=0, padx=(0, 5))

        # Generate button inside the frame, right next to the entry
        generate_button = tk.Button(password_frame, text="Generate Password", command=self.generate_pswd_btn_command)
        generate_button.grid(row=0, column=1)

        # Add button with a placeholder command
        add_button = tk.Button(self.__root, text="Add", width=36, command=self.add_data_btn_command)
        add_button.grid(row=4, column=1, columnspan=2, pady=(10, 20), padx=(0, 20), sticky="w")

        # Run the application -- not in here
        # self.__root.mainloop()

    @property
    def root(self):
        return self.__root

    @property
    def website(self):
        return self.__website_entry.get()

    @property
    def email(self):
        return self.__email_entry.get()

    @property
    def password(self):
        return self.__password_entry.get()

    def set_add_data_btn_command(self, command):
        self.__add_data_btn_command = command

    def add_data_btn_command(self):
        if self.check_messagebox():
            if self.__add_data_btn_command:
                self.__add_data_btn_command()
                self.__clean_entries()

    def set_generate_pswd_btn_command(self, command):
        self.__generate_pswd_btn_command = command

    def generate_pswd_btn_command(self):
        if self.__generate_pswd_btn_command:
            password = self.__generate_pswd_btn_command()
            self.__password_entry.delete(0, tk.END)
            self.__password_entry.insert(0, password)

            if self.__clipboard:
                self.__clipboard.copy_to_clipboard(password)

    def set_search_website_btn_command(self, command):
        if self.__search_website_btn_command:
            self.__search_website_btn_command = command

    def search_website_btn_command(self):
        if self.website:
            # Add functionality for searching
            pass
        else:
            tk.messagebox.showinfo(message="Please enter a website to search")

    def show_search_msgbox(self, search_result):
        """
        Displays the search result or an error messagein a messagebox.
        Args:
            search_result: A tuple containing (error_message, result_dict).
        """
        error_message, result = search_result

        if error_message:
            tk.messagebox.showinfo(message=error_message)
        elif result:
            tk.messagebox.showinfo(
                message=f"Website: {self.website}\n"
                        f"ID: {result['Email/Username']}\n"
                        f"PWD: {result['Password']}\n"
            )

    def __clean_entries(self):
        self.__website_entry.delete(0, tk.END)
        self.__password_entry.delete(0, tk.END)

    def check_messagebox(self):
        if not self.website:
            tk.messagebox.showinfo(message="website is missing")
            self.__website_entry.focus()
            # self.website.focus()
        elif not self.email:
            tk.messagebox.showinfo(message="email is missing")
        elif not self.password:
            tk.messagebox.showinfo(message="password is missing")
        else:
            is_double_checked = tk.messagebox.askokcancel(title="double check",
                                                          message=f"{self.website}\n"
                                                                  f"ID:{self.email}\n"
                                                                  f"PWD:{self.password}\n"
                                                                  f"Are you sure?")
            return is_double_checked

    def set_clipboard(self, clipboard):
        self.__clipboard = clipboard
