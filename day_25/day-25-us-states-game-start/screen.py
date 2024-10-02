import turtle


class Screen:
    def __init__(self):
        self.__screen = turtle.Screen()
        self.__screen.title("U.S. States Game")
        image = "blank_states_img.gif"
        self.__screen.addshape(image)
        turtle.shape(image)

    @property
    def screen(self):
        return self.__screen
