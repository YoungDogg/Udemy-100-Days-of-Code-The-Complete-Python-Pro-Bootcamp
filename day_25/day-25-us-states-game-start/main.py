from score import Score
from state_locator import StateLocator
from screen import Screen


def main():
    # Make UI: the screen, pop-up window
    screen = Screen().screen

    score = Score(screen)
    score.display_ui_all()
    stateLocator = StateLocator(screen, score)

    screen.onclick(stateLocator.return_coordinates)

    screen.mainloop()


if __name__ == "__main__":
    main()
