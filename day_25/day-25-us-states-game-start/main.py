from score import Score
from state_locator import StateLocator
from screen import Screen
from data import Data


def main():
    screen = Screen().screen
    data = Data()
    score = Score(screen, data)
    score.display_ui_all()
    stateLocator = StateLocator(screen, data, score)

    screen.onclick(stateLocator.return_coordinates)

    screen.mainloop()


if __name__ == "__main__":
    main()
