from turtle import Screen, Turtle
from typing import List


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")

    snake:List[Turtle] = []
    x_pos = 0
    for _ in range(3):
        cell = Turtle()
        cell.color("white")
        cell.shape("square")
        cell.penup()
        cell.goto(x=x_pos,y=0)
        snake.append(cell)
        x_pos += -20


    screen.mainloop()


if __name__ == '__main__':
    main()
