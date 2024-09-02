import turtle


def main():
    # Make UI: the screen, pop-up window
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)

    screen.exitonclick()


if __name__ == "__main__":
    main()