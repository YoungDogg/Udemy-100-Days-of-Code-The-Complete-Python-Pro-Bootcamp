from ui import UI
from countdown import CountDown
from timer_state import TimerState
from timer_button import UIText

WORK_MIN = 3/60
SHORT_BREAK_MIN = 5/60
LONG_BREAK_MIN = 20/60
HOW_MANY_SHORT_BREAK = 3


class Main:

    def __init__(self):
        self.__ui = UI()
        self.__timer_text = self.__ui.timer_text
        self.__canvas = self.__ui.canvas

        self.__countdown = CountDown(self.__ui.canvas,
                                     WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, HOW_MANY_SHORT_BREAK,
                                     update_ui_callback=self.__ui.update_ui_digit)
        self.__ui.set_start_callback(self.toggle_timer)
        self.__ui.set_reset_callback(self.handle_reset_process)

        self.__ui.window.mainloop()

    def toggle_timer(self):
        current_state = self.__countdown.get_state()
        if current_state == TimerState.STOPPED or current_state == TimerState.RESET:
            self.__countdown.start_timer()
            self.__ui.update_ui_start_stop_btn(UIText.STOP.value)
        elif current_state == TimerState.RUNNING:
            self.__countdown.stop_timer()
            self.__ui.update_ui_start_stop_btn(UIText.START.value)

    def handle_reset_process(self):
        # reset the time and make start button appear

        self.__countdown.reset_timer()
        # Ensure the start button is set to 'Start' after resetting
        self.__ui.update_ui_start_stop_btn(UIText.START.value)


if __name__ == '__main__':
    Main()
