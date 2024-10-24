from timer_state import WorkState


class PomoCycle:
    def __init__(self, *args, **kwargs):
        self.__countdown = args[0] if len(args) >= 1 else kwargs.get('countdown')
        self.__work_min = args[1] if len(args) >= 2 else kwargs.get('WORK_MIN', 25)
        self.__short_break_min = args[2] if len(args) >= 3 else kwargs.get('SHORT_BREAK_MIN', 5)
        self.__long_break_min = args[3] if len(args) >= 4 else kwargs.get('LONG_BREAK_MIN', 20)
        self.__how_many_short_break = args[4] if len(args) >= 5 else kwargs.get('HOW_MANY_SHORT_BREAK', 3)

        self.__currnt_left_short_break = self.__how_many_short_break
        self.__work_state = WorkState.WORK
        self.__given_time = 1  # for the test
        # self.__given_time = self.__work_min  # for the test

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
            self.__currnt_left_short_break = self.__how_many_short_break # Reset short break counter
        elif self.__work_state == WorkState.RESET:
            print('reset')
            self.__currnt_left_short_break = self.__how_many_short_break  # Reset short break counter

    def handle_work_phase_complete(self):
        if self.__currnt_left_short_break > 0:
            self.__currnt_left_short_break -= 1
            self.move_to_short_break_phase()
        else:
            self.move_to_long_break_phase()

    def move_to_work_phase(self):
        self.__work_state = WorkState.WORK
        # self.__given_time = 1  # for the test
        print(f'=== work {4-self.__currnt_left_short_break} ===')
        self.__countdown.start_timer(self.__work_min * 60, self.manage_phase_sequence)

    def move_to_short_break_phase(self):
        self.__work_state = WorkState.SHORTBREAK

        # self.__given_time = 3  # for the test
        print(f'=== short_break {3 - self.__currnt_left_short_break} ===')
        self.__countdown.start_timer(self.__short_break_min * 60, self.manage_phase_sequence)

    def move_to_long_break_phase(self):
        self.__work_state = WorkState.LONGBREAK
        # self.__given_time = self.__long_break_min * 60
        print('=== long_break ===')
        self.__countdown.start_timer(self.__long_break_min * 60, self.manage_phase_sequence)

    def move_to_reset_phase(self):
        self.__work_state = WorkState.RESET
        self.__currnt_left_short_break = self.__how_many_short_break
        self.__countdown.stop_timer()
        self.__countdown.reset_timer(self.__work_min * 60)
        print('=== reset ===')


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
