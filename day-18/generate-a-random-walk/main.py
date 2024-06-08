from MyTurtle import MyTurtle
from turtle import Screen

def main():
    turtle = MyTurtle()
    screen = Screen()

    screen.colormode(255)
    try:
        turtle.move("joi")
    except ValueError as e:
        print(e)

    screen.mainloop()

if __name__ == "__main__":
    main()





