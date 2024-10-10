import tkinter as tk
from tkinter import ttk
from countdown import CountDown

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = 'white'
BLACK = 'black'
FONT_NAME = "Courier"
BUTTON_STYLE = 'TButton'
CHECK_STYLE = 'TLabel'
WORK_MIN = 24
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
HOW_MANY_SHORT_BREAK = 3


def main():
    window = tk.Tk()

    # ---------------------------- TIMER RESET ------------------------------- #

    # ---------------------------- TIMER MECHANISM ------------------------------- #

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

    # ---------------------------- UI SETUP ------------------------------- #

    window.title('Pomodoro')
    window.config(padx=100, pady=50, bg=YELLOW)

    style = ttk.Style()
    style.configure(BUTTON_STYLE, font=(FONT_NAME, 12, 'bold'))
    style.configure(CHECK_STYLE, font=(FONT_NAME, 12, 'bold'), )

    canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = tk.PhotoImage(file='img/tomato.png')
    canvas.create_image(100, 110, image=tomato_img)
    timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, '35', 'bold'))
    canvas.grid(row=1, column=1)

    title = ttk.Label(window, text='Timer', font=(FONT_NAME, '42'), foreground=GREEN, background=YELLOW)
    title.grid(row=0, column=1)

    start_btn = ttk.Button(window, text='Start', style=BUTTON_STYLE)
    start_btn.grid(row=2, column=0)

    reset_btn = ttk.Button(window, text='Reset', style=BUTTON_STYLE)
    reset_btn.grid(row=2, column=2)

    check_dict = {'ok': '✔️', 'fail': '❌'}
    check_mark = ttk.Label(window, text=check_dict['ok'], style=CHECK_STYLE, foreground=GREEN, background=YELLOW)
    check_mark2 = ttk.Label(window, text=check_dict['fail'], style=CHECK_STYLE, foreground=RED, background=YELLOW)
    check_mark2.grid(row=3, column=1)

    count_down = CountDown(canvas, WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN, HOW_MANY_SHORT_BREAK, timer_text)
    count_down.start_whole_process()

    window.mainloop()


if __name__ == '__main__':
    main()
