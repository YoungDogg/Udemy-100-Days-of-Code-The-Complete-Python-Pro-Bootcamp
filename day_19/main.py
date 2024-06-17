from day_19.turtle_19 import day_19_sketch_turtle
from turtle import Screen

def main():
    trt = day_19_sketch_turtle()
    scn = Screen()

    scn.listen()
    scn.onkey(key="w", fun=trt.move_forward)
    scn.onkey(key="s", fun=trt.move_backwoard)
    scn.onkey(key="a", fun=trt.rotate_anti_clock)
    scn.onkey(key="d", fun=trt.rotate_clock)
    scn.mainloop()
if __name__ == "__main__":
    main()