from tkinter import *


class UI:
    def __init__(self, **kwargs):
        self.__service = kwargs.get('service')
        self.__root = Tk()
        self.__root.geometry("300x150+10+10")
        self.__root.grid_rowconfigure([0, 1, 2], weight=1)
        self.__root.grid_columnconfigure([0, 1, 2], weight=1)

        self.__input_speed = Entry(self.__root, text="100", font=("Comic Sans MS", 8))
        self.__input_speed.grid(row=0, column=1, padx=5, pady=1, sticky="ew")

        self.__labels = {
            "miles": Label(self.__root, text="miles"),
            "is equal to": Label(self.__root, text="is equal to"),
            "output": Label(self.__root, text="output"),
            "km": Label(self.__root, text="km")
        }

        self.__labels["miles"].grid(row=0, column=2, padx=1, pady=1)
        self.__labels["is equal to"].grid(row=1, column=0, padx=1, pady=1)
        self.__labels["output"].grid(row=1, column=1, padx=1, pady=1)
        self.__labels["km"].grid(row=1, column=2, padx=1, pady=1)

        self.__calculate_btn = Button(self.__root, text="Calculate", command=lambda: self.do_btn())
        self.__calculate_btn.grid(row=2, column=1, padx=1, pady=1)

        self.__root.mainloop()

    def do_btn(self):
        print('hi')
        km = self.__service.converter_ml2km(self.input_speed)
        self.__labels["output"].config(text=str(km))

    @property
    def input_speed(self):
        if self.__input_speed.get() == '':
            return 0
        return int(self.__input_speed.get())

    @property
    def btn_command(self):
        return self.__btn_command

    @btn_command.setter
    def btn_command(self, val: str):
        self.btn_command = val


if __name__ == "__main__":
    UI()
