from countdown import CountDown


class PomoCycle:
    def __init__(self):
        self.__countdown = args[0] if len(args) >= 1 else kwargs.get('CountDown',CountDown())
        self.__work_min = args[1] if len(args) >= 2 else kwargs.get('WORK_MIN', 25)
        self.__short_break_min = args[2] if len(args) >= 3 else kwargs.get('SHORT_BREAK_MIN', 5)
        self.__long_break_min = args[3] if len(args) >= 4 else kwargs.get('LONG_BREAK_MIN', 20)
        self.__how_many_short_break = args[4] if len(args) >= 5 else kwargs.get('HOW_MANY_SHORT_BREAK', 3)
        self.__work_state = WorkState.WORK
        self.__given_time = 1  # for the test
        # self.__given_time = self.__work_min  # for the test

        def start_whole_process(self):
            self.move_to_work_phase()

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
            self.__given_time = 1  # for the test
            print('work')
            self.count_down_and_display_time()

        def move_to_short_break_phase(self):
            self.__work_state = WorkState.SHORTBREAK
            # self.__given_time = self.__short_break_min * 60
            self.__given_time = 3  # for the test
            print('short_break')
            self.count_down_and_display_time()

        def move_to_long_break_phase(self):
            self.__work_state = WorkState.LONGBREAK
            # self.__given_time = self.__long_break_min * 60
            self.__given_time = 5  # for the test
            print('long_break')
            self.count_down_and_display_time()

if __name__ == "__main__":
    pomo_cycle = PomoCycle()
