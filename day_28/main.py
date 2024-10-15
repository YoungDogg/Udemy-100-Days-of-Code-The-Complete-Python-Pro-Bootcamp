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
        self.__is_started = True

        self.__countdown = CountDown(self.__ui.canvas, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, HOW_MANY_SHORT_BREAK,
                                     update_ui_callback=self.__ui.update_ui)
        self.__ui.set_start_callback(self.toggle_timer)
        self.__ui.set_reset_callback(self.__countdown.reset_timer)

        self.__ui.window.mainloop()

    def toggle_timer(self):
        print(f'main is_started:{self.__is_started}')
        if self.__is_started:
            # stop the timer
            self.__countdown.start_timer(self.__is_started)
            self.__ui.update_start_stop_btn('stop')
        else:
            # start the timer
            self.__countdown.start_timer(self.__is_started)
            self.__ui.update_start_stop_btn('start')

        self.__is_started = not self.__is_started


if __name__ == '__main__':
    Main()
