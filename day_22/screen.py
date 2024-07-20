from turtle import Turtle, ScrolledCanvas, TurtleScreen
from tkinter import *
class Screen:
    def __init__(self, width, height):
        root = Tk()
        canvas = ScrolledCanvas(root)
        canvas.pack(side=LEFT)
        self._screen = TurtleScreen(cv=canvas)
        self.width = width
        self.height = height

    def set_screen(self):
        self._screen.screensize(canvwidth=self.width, canvheight=self.height)

    @property
    def get_screen(self):
        return self._screen.screensize()


