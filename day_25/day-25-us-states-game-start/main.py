import math
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
        clicked_coord = [x,y]
        # print(f"Clicked coordinates: {clicked_coord}")
        find_closest_state(clicked_coord)

    def find_closest_state(clicked_coord):
        # get the closest Euclidean distance and compare and return the smallest
        closet_distance = 10 ** 9
        for state in coordinate_list:
            x = (clicked_coord[0] - int(state[0])) ** 2
            y = (clicked_coord[1] - int(state[1])) ** 2
            current_distance = float(f"{math.sqrt(x + y):.2f}")
            if current_distance < closet_distance:
                closest_coord = [state[0], state[1]]
                closet_distance = current_distance
                state_name = state[2]
        print(f"clicked_coord:{clicked_coord} closest_coord: {closest_coord} "
              f"closet_distance:{closet_distance} state_name: {state_name}")



        check_state(state_name)

    def check_state(state_name):
        # input popup
        input_return = screen.textinput("Guess the State", "Name?")
        print(f"state_name: {state_name} input_return: {input_return}")
        if state_name.lower() == input_return.lower():
            # +1 score
            print("you got it")
        else:
            print("failed and game over")

    screen.onclick(return_coordinates)



    # [v] get coordinate data list
    # coordinate_x_list = list(data["x"])
    # coordinate_y_list = list(data["y"])
    # coordinate_list = []
    # for idx in range(len(coordinate_x_list)):
    #     coordinate = [coordinate_x_list[idx], coordinate_y_list[idx]]
    #     coordinate_list.append(coordinate)
    coordinate_list = [list(coord) for coord in zip(data["x"], data["y"], data["state"])]
    # print(coordinate_list)

    # condition comparing input and the state list

    screen.mainloop()


if __name__ == "__main__":
    main()