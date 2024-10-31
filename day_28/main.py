from ui import UI
from countdown import CountDown
from timer_state import TimerState
from timer_button import UIText
from pomocycle import PomoCycle


class Main:

    def __init__(self):
        # Initialize UI
        self.__ui = UI()
        self.__timer_text = self.__ui.timer_text
        self.__canvas = self.__ui.canvas

        # Initialize Countdown with UI update callback and Timer Widget
        self.__countdown = CountDown(
            update_ui_callback=self.__ui.update_ui_digit,
            canvas=self.__canvas  # it's for cavas.after()
        )
        # Initialize Pomocycle
        self.__pomocycle = PomoCycle(self.__countdown)

        # how to make the start button make start? and stop also? and what about reset?
        # set button callbacks for start/stop and reset
        self.__ui.set_start_callback(self.toggle_timer)
        self.__ui.set_reset_callback(self.handle_reset_process)

        self.__canvas.mainloop()

    def toggle_timer(self):
        # check both the timer state and work state
        timer_state = self.__countdown.get_state()
        if timer_state in [TimerState.STOPPED, TimerState.RESET]:
            if timer_state == TimerState.RESET:
                # reset the timer
                self.__pomocycle.start_pomocycle()
            elif timer_state == TimerState.STOPPED:
                # start the pomo cycle fresh
                self.__countdown.start_timer()
            self.__ui.update_ui_start_stop_btn(UIText.STOP.value)
        elif timer_state == TimerState.RUNNING:
            # stop the timer
            self.__countdown.stop_timer()
            self.__ui.update_ui_start_stop_btn(UIText.START.value)

    def handle_reset_process(self):
        # reset the pomodoro cycle and update the button state
        self.__pomocycle.move_to_reset_phase()
        self.__ui.update_ui_process_check(UIText.START.value)

        self.__ui.window.mainloop()


if __name__ == '__main__':
    m = Main()
