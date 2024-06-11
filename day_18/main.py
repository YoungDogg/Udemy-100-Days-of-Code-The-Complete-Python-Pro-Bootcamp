from generate_a_random_walk.MyTurtle import MyTurtle
from turtle import Screen
from hirst_painting.colorgram import MyColorgram

def main():
    turtle = MyTurtle()
    colorgram = MyColorgram(extract_num=100)

    screen = Screen()

    screen.colormode(255)

    try:
        # turtle.randome_move(20)
        # turtle.circling_circle(5)
        colorgram.append_color_tuple()        
        turtle.draw_dot(color_list=colorgram.color_list)
    except ValueError as e:
        print(e)

    screen.mainloop()


if __name__ == "__main__":
    main()
