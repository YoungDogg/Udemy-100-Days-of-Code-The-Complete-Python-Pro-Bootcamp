import tkinter as tk
from tkinter import messagebox
import os


class UI:
    """User Interface class for the Password Manager application."""

    def __init__(self):
        """Initializes the UI components."""
        self.logo_image = None
        self._root = None
        self._password_entry = None
        self._website_entry = None
        self._email_entry = None
        self._add_data_command = None
        self._generate_password_command = None
        self._search_website_command = None
        self._clipboard = None
        self.setup_ui()

    def setup_ui(self):
        """Sets up the main UI components of the application."""
        self._setup_root()
        self._setup_logo()
        self._setup_website_entry()
        self._setup_email_entry()
        self._setup_password_entry()
        self._setup_add_button()

    def _setup_root(self):
        """Initializes the main window and its grid layout."""
        self._root = tk.Tk()
        self._root.title("Password Manager")
        self._root.grid_columnconfigure(0, weight=1)
        self._root.grid_columnconfigure(1, weight=1)
        self._root.grid_columnconfigure(2, weight=1)

    def _setup_logo(self):
        """Loads and displays the logo image."""

        # logo_path = "../day_29/logo.png"  # Replace with your image path
        logo_path = os.path.join(os.path.dirname(__file__), "../day_29/logo.png")
        self.logo_image = tk.PhotoImage(file=logo_path)
        logo_label = tk.Label(self._root, image=self.logo_image)
        logo_label.grid(row=0, column=0, columnspan=3, pady=(20, 20), sticky="n")

    def _setup_website_entry(self):
        """Sets up the website entry field and search button."""
        website_label = tk.Label(self._root, text="Website:")
        website_label.grid(row=1, column=0, padx=(20, 10), sticky="e")
        self._website_entry = tk.Entry(self._root, width=35)
        self._website_entry.focus()
        self._website_entry.grid(row=1, column=1, padx=(0, 5), pady=(5, 5), sticky="w")

        search_button = tk.Button(self._root, text="Search", command=self._on_search_website)
        search_button.grid(row=1, column=2, padx=(5, 20), pady=(5, 5), sticky="w")

    def _setup_email_entry(self):
        """Sets up the email/username entry field."""
        email_label = tk.Label(self._root, text="Email/Username:")
        email_label.grid(row=2, column=0, padx=(20, 10), sticky="e")
        self._email_entry = tk.Entry(self._root, width=35)
        self._email_entry.insert(0, "dummy@email.com")
        self._email_entry.grid(row=2, column=1, columnspan=2, padx=(0, 20), pady=(5, 5), sticky="w")

    def _setup_password_entry(self):
        """Sets up the password entry field and generate button."""
        password_label = tk.Label(self._root, text="Password:")
        password_label.grid(row=3, column=0, padx=(20, 10), sticky="e")

        password_frame = tk.Frame(self._root)
        password_frame.grid(row=3, column=1, columnspan=2, sticky="w")

        self._password_entry = tk.Entry(password_frame, width=20)
        self._password_entry.grid(row=0, column=0, padx=(0, 5))

        generate_button = tk.Button(password_frame, text="Generate Password", command=self._on_generate_password)
        generate_button.grid(row=0, column=1)

    def _setup_add_button(self):
        """Sets up the add button."""
        add_button = tk.Button(self._root, text="Add", width=36, command=self._on_add_data)
        add_button.grid(row=4, column=1, columnspan=2, pady=(10, 20), padx=(0, 20), sticky="w")

    @property
    def root(self):
        """Returns the root Tkinter window."""
        return self._root

    @property
    def website(self):
        """Returns the website entered by the user."""
        return self._website_entry.get().strip()

    @property
    def email(self):
        """Returns the email entered by the user."""
        return self._email_entry.get().strip()

    @property
    def password(self):
        """Returns the password entered by the user."""
        return self._password_entry.get().strip()

    def set_add_data_command(self, command):
        """Sets the command to be called when adding data."""
        self._add_data_command = command

    def set_generate_password_command(self, command):
        """Sets the command to be called when generating a password."""
        self._generate_password_command = command

    def set_search_website_command(self, command):
        """Sets the command to be called when searching for a website."""
        self._search_website_command = command

    def set_clipboard(self, clipboard):
        """Sets the clipboard utility."""
        self._clipboard = clipboard

    def _on_add_data(self):
        """Callback method when the 'Add' button is clicked."""
        if self._validate_inputs():
            if self._add_data_command:
                self._add_data_command()
                self._clear_entries()
            else:
                messagebox.showwarning("Warning", "Add data command not set.")

    def _on_generate_password(self):
        """Callback method when the 'Generate Password' button is clicked."""
        if self._generate_password_command:
            password = self._generate_password_command()
            self._password_entry.delete(0, tk.END)
            self._password_entry.insert(0, password)

            if self._clipboard:
                self._clipboard.copy_to_clipboard(password)
        else:
            messagebox.showwarning("Warning", "Generate password command not set.")

    def _on_search_website(self):
        """Callback method when the 'Search' button is clicked."""
        website = self.website
        if website:
            if self._search_website_command:
                search_result = self._search_website_command(website)
                self._show_search_result(search_result)
            else:
                messagebox.showwarning("Warning", "Search command not set.")
        else:
            messagebox.showinfo("Information", "Please enter a website to search.")

    def _show_search_result(self, search_result):
        """Displays the search result in a messagebox."""
        error_message = search_result.get("message")
        result = search_result.get("data")

        if error_message:
            messagebox.showerror("Error", error_message)
        elif result:
            messagebox.showinfo(
                "Search Result",
                f"Website: {self.website}\n"
                f"Email/Username: {result['Email/Username']}\n"
                f"Password: {result['Password']}\n"
            )
        else:
            messagebox.showinfo("Information", "No data found for the given website.")

    def _validate_inputs(self):
        """Validates that all required inputs are filled."""
        if not self.website:
            messagebox.showinfo("Information", "Website is missing.")
            self._website_entry.focus()
            return False
        elif not self.email:
            messagebox.showinfo("Information", "Email is missing.")
            self._email_entry.focus()
            return False
        elif not self.password:
            messagebox.showinfo("Information", "Password is missing.")
            self._password_entry.focus()
            return False
        else:
            is_confirmed = messagebox.askokcancel(
                "Confirm Details",
                f"Website: {self.website}\n"
                f"Email: {self.email}\n"
                f"Password: {self.password}\n\n"
                "Do you want to save these details?"
            )
            return is_confirmed

    def _clear_entries(self):
        """Clears the input fields."""
        self._website_entry.delete(0, tk.END)
        self._password_entry.delete(0, tk.END)


if __name__ == "__main__":
    ui = UI()
    ui.root.mainloop()
