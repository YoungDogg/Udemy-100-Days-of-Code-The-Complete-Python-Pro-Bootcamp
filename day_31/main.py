from ui import FlashCardUI


class Main:
    def __init__(self):
        ui = FlashCardUI()


if __name__ == '__main__':
    main_app = Main()
    main_app.ui.root.mainloop()