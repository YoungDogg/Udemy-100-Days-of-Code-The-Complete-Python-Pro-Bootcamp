import tkinter as tk
from tkinter import ttk

from enum import Enum


class UIText(Enum):
    TITLE="단어 맞추기"
    GAMEOVER="잘했어요"
    BGCOLOR = '#f7f5dd'


class UI:
    """Displays the deck UI"""
    def __init__(self):
        self._window = None
        self._canvas = None
        self.card = None
        self.v_button = None
        self.x_button = None
        self._set_up()

    @property
    def window(self):
        return self._window

    @property
    def canvas(self):
        return self._canvas

    def _set_up(self):
        # self._set_window()
        self._set_canvas()
        # self._set_card()

    def _set_window(self):
        self._window = tk.Tk()
        self._window.title(UIText.TITLE.value)
        self._window.grid_rowconfigure([0, 1], weight=1)
        self._window.grid_columnconfigure([0, 1, 2], weight=1)

    def _set_canvas(self):
        self._canvas = tk.Canvas(width=200, height=224, bg=UIText.BGCOLOR.value)

    def _set_card(self):
        self.card = self._window.frame()


if __name__ == '__main__':
    ui = UI()
    ui.canvas.mainloop()
