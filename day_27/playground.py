from tkinter import *


def main():
    # make a new button using grid
    root = Tk()
    root.title("day 26")
    root.geometry("500x500")


    label = Label(root, text="Hello", font=("Arial", 16))
    label.grid(row=0, column=0)
    label.config(padx=10,pady=20)

    def print_new_button():
        print("new button")
    new_button = Button(root, text="new button", command=print_new_button)
    new_button.grid(row=0, column=2)


    def print_button():
        print("button")
    button = Button(root, text="button", command=print_button)
    button.grid(row=1, column=1)

    entry = Entry(root, width=30)
    print(entry.get())
    entry.grid(row=2, column=3)

    root.mainloop()

if __name__ == "__main__":
    main()