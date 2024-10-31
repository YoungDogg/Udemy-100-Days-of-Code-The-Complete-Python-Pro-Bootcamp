import time
from timer_state import TimerState
from typing import Callable, Optional
from tkinter import Canvas


class CountDown:
    def __init__(self, *args, **kwargs):
        self.__update_ui_digit_callback: Callable[[str], None] = args[0] \
            if len(args) >= 1 else kwargs.get('update_ui_callback')
        self.__canvas: Canvas = args[1] if len(args) >= 2 else kwargs.get('canvas')

        self.__phase_complete_callback: Optional[Callable[[], None]] = None
        self.__given_time = 0
        self.__state = TimerState.RESET

    def get_state(self):
        return self.__state

    def count_down_and_display_time(self):
        count_min = self.__given_time // 60
        count_sec = self.__given_time % 60

        current_time = time.strftime('%H:%M:%S')
        print(f'{self.__state}==== {count_min:02}:{count_sec:02} || Real-time: {current_time}')

        self.__update_ui_digit_callback(f'{count_min:02}:{count_sec:02}')

        if self.__state != TimerState.RUNNING:
            return

        if self.__given_time > 0:
            self.__given_time -= 1
            self.__canvas.after(1 * 1000, self.count_down_and_display_time)
        else:
            self.stop_timer()
            if self.__phase_complete_callback:
                self.__phase_complete_callback()

    def start_timer(self, time_in_min: int = None, phase_complete_callback: Optional[Callable[[], None]] = None):
        if time_in_min is not None:
            # set __given_time only if the timer is rest, starting fresh
            self.__given_time = time_in_min

        self.__state = TimerState.RUNNING
        print('timer started')
        self.__phase_complete_callback = phase_complete_callback
        self.count_down_and_display_time()

    def stop_timer(self):
        self.__state = TimerState.STOPPED
        print('timer stopped')

    def reset_timer(self, time_in_min: int):
        self.__state = TimerState.RESET
        self.__given_time = time_in_min
        count_min = self.__given_time // 60
        count_sec = self.__given_time % 60
        self.__update_ui_digit_callback(f'{count_min:02}:{count_sec:02}')
        print('timer reset')


if __name__ == "__main__":
    from tkinter import Tk


    def mock_update_ui(time_string):
        """Mock function to simulate UI update by printing the time."""
        print(f"Mock UI Update: {time_string}")


    countdown = CountDown(mock_update_ui, Tk())

    print('Starting 1 min timer')
    countdown.start_timer(1)

    time.sleep(3)
    print('Stopping timer')
    countdown.stop_timer()

    print('Restting timer')
    countdown.reset_timer(1)
