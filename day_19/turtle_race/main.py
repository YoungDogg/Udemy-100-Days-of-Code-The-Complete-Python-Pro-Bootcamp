from turtle import Screen
from day_19.turtle_race.day_19_turtle_race import  TurtleRaceUnit

def main():
    scn = Screen()
    scn.screensize(canvwidth=500, canvheight=400)

    turt = TurtleRaceUnit(color="red")

    scn.mainloop()


if __name__ == '__main__':
    main()
