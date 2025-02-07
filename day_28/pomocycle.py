from timer_state import WorkState
from timer_state import HowManyTimes

Min = 2


class PomoCycle:
    def __init__(self, *args, **kwargs):
        self.__countdown = args[0] if len(args) >= 1 else kwargs.get('countdown')
        self.__update_ui_state_callback = args[1] if len(args) >= 2 else kwargs.get('update_ui_state_callback')

        self.__work_min = HowManyTimes.WORK_MIN.value
        self.__short_break_min = HowManyTimes.SHORT_BREAK_MIN.value * Min
        self.__long_break_min = HowManyTimes.LONG_BREAK_MIN.value * Min
        self.__how_many_work = HowManyTimes.HOW_MANY_TIME_TO_WORK.value
        self.__how_many_short_break = HowManyTimes.HOW_MANY_TIME_TO_WORK.value - 1
        self.__current_short_break_count = self.__current_work_count = 0
        self.__work_state = WorkState.WORK
        self.__pomo_state: dict[WorkState, int] = {WorkState.WORK: 0, WorkState.SHORTBREAK: 0, WorkState.LONGBREAK: 0}
        self.__given_time = 0

    def start_pomocycle(self):
        self.move_to_work_phase()

    def manage_phase_sequence(self):
        """manage the phase transitions (work->break->work)"""
        if self.__work_state == WorkState.WORK:
            self.handle_work_phase_complete()
        elif self.__work_state == WorkState.SHORTBREAK:
            self.move_to_work_phase()
        elif self.__work_state == WorkState.LONGBREAK:
            print(f'whole phases completed!')
            print(f'Do this again until press start or reset')
            self.__current_short_break_count = 0
            self.__current_work_count = 0
            self.__work_state = WorkState.RESET  # reset the state
        elif self.__work_state == WorkState.RESET:
            print('reset')

    def handle_work_phase_complete(self):
        if self.__current_short_break_count < self.__how_many_short_break:
            print(f'=== {WorkState.SHORTBREAK} {self.__current_short_break_count} ===')
            self.move_to_short_break_phase()
        else:
            print(f'=== {WorkState.LONGBREAK} {self.__current_short_break_count} ===')
            self.move_to_long_break_phase()

    def move_to_work_phase(self):
        if self.__current_work_count < self.__how_many_work:
            print(f'=== {WorkState.WORK} {self.__current_work_count} ===')
            self.__work_state = WorkState.WORK
            self.__pomo_state[self.__work_state] = self.__current_work_count
            self.__current_work_count += 1  # increment work phase count properly
            self.update_ui_state()
            self.__countdown.start_timer(self.__work_min, self.manage_phase_sequence)
        else:
            self.__work_state = WorkState.LONGBREAK
            self.manage_phase_sequence()

    def move_to_short_break_phase(self):
        self.__work_state = WorkState.SHORTBREAK
        self.__pomo_state[self.__work_state] = self.__current_work_count
        self.update_ui_state()
        self.__current_short_break_count += 1
        self.__countdown.start_timer(self.__short_break_min, self.manage_phase_sequence)

    def move_to_long_break_phase(self):
        self.__work_state = WorkState.LONGBREAK
        self.__pomo_state[self.__work_state] = self.__current_work_count
        self.update_ui_state()
        self.__countdown.start_timer(self.__long_break_min, self.manage_phase_sequence)

    def move_to_reset_phase(self):
        print('=== reset ===')
        self.__work_state = WorkState.RESET
        self.__current_short_break_count = 0
        self.__current_work_count = 0
        self.__countdown.stop_timer()
        self.__countdown.reset_timer(self.__work_min)

    def get_work_state(self):
        return self.__work_state

    def get_current_work_progress(self):
        return self.__current_work_count

    def get_pomo_state(self):
        return self.__pomo_state

    def update_ui_state(self):
        #  current work and break state callback
        if self.__update_ui_state_callback:
            self.__update_ui_state_callback(self.__pomo_state, self.__work_state)


if __name__ == "__main__":
    from countdown import CountDown
    from tkinter import Tk

    root = Tk()


    def mock_update_ui(time_string):
        """Mock function to simulate UI update by printing the time."""
        print(f"Mock UI Update: {time_string}")


    pomocycle = PomoCycle(
        countdown=CountDown(mock_update_ui, root),
        WORK_MIN=1 / 60,
        SHORT_BREAK_MIN=1 / 60,
        LONG_BREAK_MIN=1 / 60,
        HOW_MANY_SHORT_BREAK=3)

    pomocycle.start_pomocycle()

    root.mainloop()
