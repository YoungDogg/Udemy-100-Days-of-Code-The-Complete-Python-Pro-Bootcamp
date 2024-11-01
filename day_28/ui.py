import tkinter as tk
from tkinter import ttk
from countdown import CountDown
from timer_button import UIText
from timer_state import HowManyTimes

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = 'white'
BLACK = 'black'
FONT_NAME = "Courier"
BUTTON_STYLE = 'TButton'
CHECK_STYLE = 'TLabel'


class UI:
    def __init__(self):
        self.__window = tk.Tk()

        self.__window.title(UIText.TITLE.value)
        self.__window.config(padx=100, pady=50, bg=YELLOW)

        self.__style = ttk.Style()
        self.__style.configure(BUTTON_STYLE, font=(FONT_NAME, 12, 'bold'))
        self.__style.configure(CHECK_STYLE, font=(FONT_NAME, 12, 'bold'), )

        self.__canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.__tomato_img = tk.PhotoImage(file='img/tomato.png')
        self.__canvas.create_image(100, 110, image=self.__tomato_img)
        self.__timer_text = self.__canvas.create_text(103, 130, text='00:00', fill='white',
                                                      font=(FONT_NAME, '35', 'bold'))
        self.__canvas.grid(row=1, column=1)

        self.__title = ttk.Label(self.__window, text=UIText.LABEL.value, font=(FONT_NAME, '42'), foreground=GREEN,
                                 background=YELLOW)
        self.__title.grid(row=0, column=1)

        self.__start_btn_command = None
        self.__start_btn = ttk.Button(self.__window, text=UIText.START.value,
                                      style=BUTTON_STYLE, command=self.start_btn_command)
        self.__start_btn.grid(row=2, column=0)

        self.__reset_btn_command = None
        self.__reset_btn = ttk.Button(self.__window, text=UIText.RESET.value, style=BUTTON_STYLE,
                                      command=self.reset_btn_command)
        self.__reset_btn.grid(row=2, column=2)

        self.__work_break_display = {'works':[], 'breaks':[]}
        for idx in range(HowManyTimes.HOW_MANY_TIME_TO_WORK.value):
            temp_work = ttk.Label(self.__window, text=UIText.WORK.value, style=CHECK_STYLE,
                                  foreground=BLACK, background=YELLOW)
            if idx == HowManyTimes.HOW_MANY_TIME_TO_WORK.value - 1:
                temp_break = ttk.Label(self.__window, text=UIText.LONGBREAK.value, style=CHECK_STYLE,
                                       foreground=BLACK, background=YELLOW)
            else:
                temp_break = ttk.Label(self.__window, text=UIText.SHORTBREAK.value, style=CHECK_STYLE,
                                       foreground=BLACK, background=YELLOW)
            temp_work.grid(row=3, column=idx)
            temp_break.grid(row=4, column=idx)
            self.__work_break_display['works'].append(temp_work)
            self.__work_break_display['breaks'].append(temp_break)

    @property
    def window(self):
        return self.__window

    @property
    def canvas(self):
        return self.__canvas

    @property
    def timer_text(self):
        return self.__timer_text

    def set_start_callback(self, callback):
        self.__start_btn_command = callback

    def set_reset_callback(self, callback):
        self.__reset_btn_command = callback

    def start_btn_command(self):
        if self.__start_btn_command:
            self.__start_btn_command()

    def reset_btn_command(self):
        if self.__reset_btn_command:
            self.__reset_btn_command()

    def update_ui_start_stop_btn(self, text):
        self.__start_btn.config(text=text)

    def update_ui_digit(self, time_string):
        # Update the UI with new timer value
        self.canvas.itemconfig(self.__timer_text, text=time_string)

    def update_ui_process_check(self, text):
        self.__work_break_display.config(text=text)

    def update_ui_work_break_display(self):
        # current state background PINK, done states background GREEN
        pass

if __name__ == '__main__':
    ui = UI()
    ui.window.mainloop()
