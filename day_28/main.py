from ui import UI
from countdown import CountDown

WORK_MIN = 24
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
HOW_MANY_SHORT_BREAK = 3


class Main:

    def __init__(self):
        self.__ui = UI()
        self.__timer_text = self.__ui.timer_text
        self.__canvas = self.__ui.canvas
        count_down = CountDown(self.__ui.canvas, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, HOW_MANY_SHORT_BREAK,
                               update_ui_callback=self.update_ui)
        count_down.start_whole_process()
        self.__ui.set_start_callback(count_down.stop_timer)
        self.__ui.set_reset_callback(count_down.reset_timer)

        self.__ui.window.mainloop()

    def update_ui(self, time_string):
        # Update the UI with new timer value
        self.__canvas.itemconfig(self.__timer_text, text=time_string)


if __name__ == '__main__':
    Main()
