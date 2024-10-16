import tkinter as tk
from tkinter import ttk
import time
from timer_state import *


class CountDown:
    def __init__(self, *args, **kwargs):
        self.__canvas = args[0] if len(args) >= 1 else kwargs.get('canvas')
        self.__work_min = args[1] if len(args) >= 2 else kwargs.get('WORK_MIN', 25)
        self.__short_break_min = args[2] if len(args) >= 3 else kwargs.get('SHORT_BREAK_MIN', 5)
        self.__long_break_min = args[3] if len(args) >= 4 else kwargs.get('LONG_BREAK_MIN', 20)
        self.__how_many_short_break = args[4] if len(args) >= 5 else kwargs.get('HOW_MANY_SHORT_BREAK', 3)
        self.__timer_text = args[5] if len(args) >= 6 else kwargs.get('timer_text')
        self.__update_ui_digit_callback = args[6] if len(args) >= 7 else kwargs.get('update_ui_callback')

        self.__is_started = False

        self.__state = TimerState.STOPPED
        self.__work_state = WorkState.WORK
        # self.__given_time = self.__work_min * 60  # initialize as work time as sec
        self.__given_time = 1  # for the test
        # self.__given_time = self.__work_min  # for the test

    @property
    def canvas(self):
        return self.__canvas

    @canvas.setter
    def canvas(self, root):
        self.__canvas = root

    def start_whole_process(self):
        self.move_to_work_phase()

    def count_down_and_display_time(self, is_started):
        if self.__state != TimerState.RUNNING:
            # print('countdown stopped.')
            return

        count_min = self.__given_time // 60
        count_sec = self.__given_time % 60

        # current_time = time.strftime('%H:%M:%S')
        # print(f'{self.__work_state}==== {count_min:02}:{count_sec:02} || Real-time: {current_time}')
        # self.canvas.itemconfig(self.__timer_text, text=f'{count_min:02}:{count_sec:02}')
        self.__update_ui_digit_callback(f'{count_min:02}:{count_sec:02}')

        if self.__given_time > 0:
            self.__given_time -= 1
            self.canvas.after(1 * 1000, lambda: self.count_down_and_display_time(is_started))
        else:
            self.manage_phase_sequence()

    def manage_phase_sequence(self):
        if self.__work_state == WorkState.WORK:
            self.handle_work_phase_complete()
        elif self.__work_state == WorkState.SHORTBREAK:
            self.move_to_work_phase()
        elif self.__work_state == WorkState.LONGBREAK:
            print(f'whole phases completed!')
            print(f'Do this again until press start or reset')
            self.__how_many_short_break = 3

    def handle_work_phase_complete(self):
        if self.__how_many_short_break > 0:
            self.__how_many_short_break -= 1
            self.move_to_short_break_phase()
        else:
            self.move_to_long_break_phase()

    def move_to_work_phase(self):
        self.__work_state = WorkState.WORK
        # self.__given_time = self.__work_min * 60
        self.__given_time = 1    # for the test
        print('work')
        self.count_down_and_display_time(True)

    def move_to_short_break_phase(self):
        self.__work_state = WorkState.SHORTBREAK
        # self.__given_time = self.__short_break_min * 60
        self.__given_time = 3   # for the test
        print('short_break')
        self.count_down_and_display_time(True)

    def move_to_long_break_phase(self):
        self.__work_state = WorkState.LONGBREAK
        # self.__given_time = self.__long_break_min * 60
        self.__given_time = 5   # for the test
        print('long_break')
        self.count_down_and_display_time(True)

    def start_timer(self):
        self.__state = TimerState.RUNNING
        print('timer started')
        self.count_down_and_display_time(True)

    def stop_timer(self):
        self.__state = TimerState.STOPPED
        print('timer stopped')

    def reset_timer(self):
        self.__state = TimerState.RESET
        self.__work_state = WorkState.WORK
        # self.__given_time = self.__work_min * 60
        self.__given_time = 1  # for the test
        self.__update_ui_digit_callback(f'{self.__given_time // 60:02}:{0:02}')
        print('timer reset')

    def get_state(self):
        return self.__state


if __name__ == "__main__":
    count_down = CountDown(25, 1, 20)
    count_down.canvas = tk.Tk()  # it's window though... only for the test...
    count_down.start_whole_process()
    count_down.canvas.mainloop()
