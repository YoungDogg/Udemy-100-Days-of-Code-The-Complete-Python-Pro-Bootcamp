from ui import UI


class Clipboard:
    def __init__(self, ui):
        self.__root = ui.root

    def copy_to_clipboard(self, text):
        self.__root.clipboard_clear()
        self.__root.clipboard_append(text)
        self.__root.update()
        print(f'pasted clipboard: {text}')


