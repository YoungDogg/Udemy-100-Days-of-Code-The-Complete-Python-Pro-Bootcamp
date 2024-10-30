from enum import Enum


class TimerState(Enum):
    STOPPED = 0
    RUNNING = 1
    RESET = 2


class WorkState(Enum):
    WORK = 1
    SHORTBREAK = 0
    LONGBREAK = -1
    RESET = -2


class HowManyTimes(Enum):
    WORK_MIN = 3 / 60
    SHORT_BREAK_MIN = 5 / 60
    LONG_BREAK_MIN = 20 / 60
    HOW_MANY_SHORT_BREAK = 3
