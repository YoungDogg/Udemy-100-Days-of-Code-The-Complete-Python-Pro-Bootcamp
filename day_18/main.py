from generate_a_random_walk.MyTurtle import MyTurtle
from turtle import Screen

def main():
    turtle = MyTurtle()


    screen = Screen()

    screen.colormode(255)

    try:
        # turtle.random_move(20)
        # turtle.circling_circle(5)
        turtle.draw_dot()
    except ValueError as e:
        print(e)

    screen.mainloop()


if __name__ == "__main__":
    main()
