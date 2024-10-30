from timer_state import WorkState
from timer_state import HowManyTimes


class PomoCycle:
    def __init__(self, *args, **kwargs):
        self.__countdown = args[0] if len(args) >= 1 else kwargs.get('countdown')

        self.__work_min = HowManyTimes.WORK_MIN
        self.__short_break_min = HowManyTimes.SHORT_BREAK_MIN
        self.__long_break_min = HowManyTimes.LONG_BREAK_MIN
        self.__how_many_short_break = HowManyTimes.HOW_MANY_SHORT_BREAK
        self.__currnt_short_break_count = 0
        self.__current_work_count = self.__currnt_short_break_count
        self.__work_state = WorkState.WORK
        self.__given_time = 0

    def start_whole_process(self):
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
            self.__currnt_short_break_count = self.__how_many_short_break # Reset short break counter
        elif self.__work_state == WorkState.RESET:
            print('reset')
            self.__currnt_short_break_count = self.__how_many_short_break  # Reset short break counter

    def handle_work_phase_complete(self):
        if self.__currnt_short_break_count < self.__how_many_short_break:
            self.__currnt_short_break_count += 1
            self.move_to_short_break_phase()
        else:
            self.move_to_long_break_phase()

    def move_to_work_phase(self):
        print(f'=== work {4-self.__currnt_short_break_count} ===')
        self.__work_state = WorkState.WORK
        self.__countdown.start_timer(self.__work_min * 60, self.manage_phase_sequence)

    def move_to_short_break_phase(self):
        print(f'=== short_break {3 - self.__currnt_short_break_count} ===')
        self.__work_state = WorkState.SHORTBREAK
        self.__countdown.start_timer(self.__short_break_min * 60, self.manage_phase_sequence)

    def move_to_long_break_phase(self):
        print('=== long_break ===')
        self.__work_state = WorkState.LONGBREAK
        self.__countdown.start_timer(self.__long_break_min * 60, self.manage_phase_sequence)

    def move_to_reset_phase(self):
        print('=== reset ===')
        self.__work_state = WorkState.RESET
        self.__currnt_short_break_count = self.__how_many_short_break
        self.__countdown.stop_timer()
        self.__countdown.reset_timer(self.__work_min * 60)

    def get_work_state(self):
        return self.__work_state

    def get_current_work_progress(self):
        return self.__current_work_count

if __name__ == "__main__":
    from countdown import CountDown
    from tkinter import Tk

    root = Tk()

    def mock_update_ui(time_string):
        """Mock function to simulate UI update by printing the time."""
        print(f"Mock UI Update: {time_string}")


    pomocycle = PomoCycle(
        countdown=CountDown(mock_update_ui, root),
        WORK_MIN=1/60,
        SHORT_BREAK_MIN=1/60,
        LONG_BREAK_MIN=1/60,
        HOW_MANY_SHORT_BREAK=3)

    pomocycle.start_whole_process()

    root.mainloop()
