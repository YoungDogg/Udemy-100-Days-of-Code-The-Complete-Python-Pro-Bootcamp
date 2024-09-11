import turtle
import pandas
import tkinter

def main():
    # Make UI: the screen, pop-up window
    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = "blank_states_img.gif"
    screen.addshape(image)

    turtle.shape(image)
    # [v] Check if the guess is among the 50 states
    # [v] get the list the states
    data = pandas.read_csv("50_states.csv")
    state_list = list(data["state"])

    # Write correct guesses onto the map
    # [v] get game screen coordinate by clicking
    def return_coordinates(x,y):
        print(f"Clicked coordinates: ({x}, {y})")

    screen.onclick(return_coordinates)

    # [v] get coordinate data list
    # coordinate_x_list = list(data["x"])
    # coordinate_y_list = list(data["y"])
    # coordinate_list = []
    # for idx in range(len(coordinate_x_list)):
    #     coordinate = [coordinate_x_list[idx], coordinate_y_list[idx]]
    #     coordinate_list.append(coordinate)
    coordinate_list = [list(coord) for coord in zip(data["x"], data["y"])]
    print(coordinate_list)


    # input popup
    input_return = screen.textinput("Guess the State", "Name?").lower()
    print(input_return)

    screen.mainloop()


if __name__ == "__main__":
    main()