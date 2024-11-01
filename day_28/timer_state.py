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
    WORK_MIN = 2
    SHORT_BREAK_MIN = 3
    LONG_BREAK_MIN = 6
    HOW_MANY_TIME_TO_WORK = 3
