from ui import UI
from data_manage import DataManage
from password_generator import PasswordGenerator
from store_to_clipboard import Clipboard


class Main:
    # def __init__(self):
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # required: button action, pandas saving, delete entries(except email)
    def __init__(self):
        self.ui = UI()
        self.pwd = PasswordGenerator()
        self.data_manage = None
        self.clipboard = None

    def set_up(self):

        # def set_class(self):
        self.ui.setup_ui()

        self.data_manage = DataManage(self.ui)
        self.clipboard = Clipboard(self.ui)

        self.data_manage.load_or_init_data()

        # def set_function(self):
        self.ui.set_add_data_btn_command(self.data_manage.save_data2file)
        self.ui.set_generate_pswd_btn_command(self.pwd.generate_pwd)
        self.ui.set_clipboard(self.clipboard)


if __name__ == '__main__':
    m = Main()
    m.set_up()
    m.ui.root.mainloop()
