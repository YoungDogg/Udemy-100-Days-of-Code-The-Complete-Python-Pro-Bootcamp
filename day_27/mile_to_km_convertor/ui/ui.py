from tkinter import *


class UI:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("300x150+10+10")
        self.root.grid_rowconfigure([0, 1, 2], weight=1)
        self.root.grid_columnconfigure([0, 1, 2], weight=1)

        self.input_speed = Entry(self.root, text="100", font=("Comic Sans MS", 8))
        self.input_speed.grid(row=0, column=1, padx=5, pady=1, sticky="ew")
        # self.input_speed.get()

        self.labels = {
            "miles": Label(text="miles"),
            "is equal to": Label(text="is equal to"),
            "output": Label(text="output"),
            "km": Label(text="km")
        }
        self.labels["miles"].grid(row=0, column=2, padx=1, pady=1)
        self.labels["is equal to"].grid(row=1, column=0, padx=1, pady=1)
        self.labels["output"].grid(row=1, column=1, padx=1, pady=1)
        self.labels["km"].grid(row=1, column=2, padx=1, pady=1)

        self.btn_command = ""
        self.calculate_btn = Button(self.root, text="Calculate", command=self.btn_command)
        self.calculate_btn.grid(row=2, column=1, padx=1, pady=1)

        self.root.mainloop()

    @property
    def btn_command(self):
        return self.btn_command

    @btn_command.setter
    def btn_command(self, val: str):
        self.btn_command = val


if __name__ == "__main__":
    UI()
