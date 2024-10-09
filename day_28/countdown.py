import tkinter as tk
from tkinter import ttk


class CountDown:
    def __init__(self, *args, **kwargs):
        if len(args) >= 1:
            self.__work_min = args[0]
        else:
            self.__work_min = kwargs.get('WORK_MIN', 25)
        if len(args) >= 2:
            self.__short_break_min = args[1]
        else:
            self.__short_break_min = kwargs.get('SHORT_BREAK_MIN', 5)
        if len(args) >= 3:
            self.__long_break_min = args[2]
        else:
            self.__long_break_min = kwargs.get('LONG_BREAK_MIN', 20)
        if len(args) >= 4:
            self.__how_many_short_break = args[3]
        else:
            self.__how_many_short_break = kwargs.get('HOW_MANY_SHORT_BREAK', 3)
        if len(args) >= 5:
            self.__window = args[4]
        else:
            self.__window = kwargs.get('window', tk.Tk())

        self.__work_state = 'work'  # or short, long break
        self.__given_time = self.__work_min * 60 # initialize as work time as sec

    def manage_work_break_short_long(self):
        is_start_btn_pressed = False    # pressed once and twice
        is_reset_btn_pressed = False

        for _ in range(self.__how_many_short_break):
            self.count_work()
            self.count_short_break()
        self.count_work()
        self.count_long_break()

    def count_work(self):
        self.__work_state = 'work'
        # self.__given_time = self.__work_min * 60
        self.__given_time = 10
        self.count_down_and_display_time()

    def count_short_break(self):
        self.__work_state = 'short_break'
        # self.__given_time = self.__short_break_min * 60
        self.__given_time = 3
        self.count_down_and_display_time()

    def count_long_break(self):
        self.__work_state = 'long_break'
        # self.__given_time = self.__long_break_min * 60
        self.__given_time = 5
        self.count_down_and_display_time()

    def count_down_and_display_time(self):
        count_min = self.__given_time // 60
        count_sec = self.__given_time % 60
        # self.__window.canvas.itemconfig(timer_text, text=f'{count_min:02}:{count_sec:02}')

        if self.__given_time > 0:
            self.__given_time += -1
            print(f'{self.__work_state}==== {count_min}:{count_sec}')
            self.__window.after(1 * 1000, self.count_down_and_display_time)


if __name__ == "__main__":
    count_down = CountDown(25, 1, 20)
    count_down.manage_work_break_short_long()
