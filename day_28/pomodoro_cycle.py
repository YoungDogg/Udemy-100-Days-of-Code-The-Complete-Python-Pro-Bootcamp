class PomodoroCycle:
    # manage the cylcle of work and break.
    # whole cycle: 4 work with 3 short breaks and 1 long break at last
    def __init__(self):
        # self.__how_many_short_break = args[0] if len(args) >= 1 else kwargs.get('HOW_MANY_SHORT_BREAK', 3)
        self.__work_count = args[0] if len(args) >= 1 else kwargs.get('WORK_COUNT', 4)
    #  decrement works after work, move to short break
    #  if work left only one, move to long break next
    pass
