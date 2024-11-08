from ui import UI
from data_manage import DataManage
from password_generator import PasswordGenrator
from store_to_clipboard import Clipboard


class Main:
    # def __init__(self):
        # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    pwd = PasswordGenrator()
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # required: button action, pandas saving, delete entries(except email)
    ui = UI()
    data_manage = None
    clipboard = None

    # def set_class(self):
    ui.setup_ui()

    data_manage = DataManage(ui)
    clipboard = Clipboard(ui)

    data_manage.load_or_init_data()

    # def set_function(self):
    ui.set_add_data_btn_command(data_manage.save_data2file)
    ui.set_generate_pswd_btn_command(pwd.generate_pwd)
    ui.set_clipboard(clipboard)


if __name__ == '__main__':
    m = Main()
    # m.set_class()
    # m.set_function()

