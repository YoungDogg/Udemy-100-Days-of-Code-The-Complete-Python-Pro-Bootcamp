import tkinter as tk


class Main:
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    # ---------------------------- UI SETUP ------------------------------- #
    def __init__(self):
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
        website_entry.grid(row=1, column=1, columnspan=2, padx=(0, 20), pady=(5, 5), sticky="w")

        # Email/Username label and entry
        email_label = tk.Label(root, text="Email/Username:")
        email_label.grid(row=2, column=0, padx=(20, 10), sticky="e")
        email_entry = tk.Entry(root, width=35)
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
        add_button = tk.Button(root, text="Add", width=36)
        add_button.grid(row=4, column=1, columnspan=2, pady=(10, 20), padx=(0, 20), sticky="w")

        # Run the application
        root.mainloop()


if __name__ == '__main__':
    m = Main()

