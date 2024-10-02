from singleton import GlobalValue
import turtle


class Score:
    def __init__(self, screen, data):
        self.__screen = screen
        self.__data = data
        self.__score = GlobalValue().value
        self.__score_ui = self.generate_UI_obj()
        self.__score_ui2 = self.generate_UI_obj()
        self.__highest_score_ui = self.generate_UI_obj()
        self.__highest_score_ui2 = self.generate_UI_obj()
        self.__gameover_ui = self.generate_UI_obj()

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, val: int):
        self.__score = val

    def increment_score(self):
        self.score += 1

    # make the score
    # UI
    @staticmethod
    def generate_UI_obj():
        ui_obj = turtle.Turtle()
        ui_obj.hideturtle()
        ui_obj.penup()
        ui_obj.speed(10)
        return ui_obj

    def display_ui_all(self):
        self.display_ui(self.__score_ui2, "score: ", 50, 70)
        self.display_ui(self.__score_ui, self.score, 62, 70)
        self.display_ui(self.__highest_score_ui, "highest: ", 45, 80)
        self.display_ui(self.__highest_score_ui2, self.__data.highest_score, 62, 80)

    def display_ui(self, ui_obj, text, width, height, x0y0=False):
        ui_obj_width = (self.__screen.window_width() / 2) * width / 100
        ui_obj_height = (self.__screen.window_height() / 2) * height / 100
        ui_obj.clear()
        if not x0y0:
            ui_obj.goto(ui_obj_width, ui_obj_height)
            ui_obj.write(text, align="left", font=('Arial', 12, 'bold'))
        else:
            ui_obj.write(text, align="center", font=('Arial', 36, 'bold'))

    def display_gameover(self):
        self.display_ui(self.__gameover_ui, "game over", 0, 0, True)
