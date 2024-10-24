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
