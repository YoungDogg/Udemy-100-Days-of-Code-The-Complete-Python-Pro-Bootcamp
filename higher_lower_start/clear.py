import os

def clear_screen():
    """Clear the command line screen."""
    # Check if the system is Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        # Assume Unix or Linux
        os.system('clear')

# Example usage:
# if __name__ == '__main__':
#     print("This is some text.")
#     input("Press Enter to clear the screen...")
#     clear_screen()
#     print("The screen has been cleared.")
