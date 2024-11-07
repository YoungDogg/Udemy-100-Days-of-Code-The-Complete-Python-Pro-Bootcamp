from ui import UI
from data_manage import DataManage


class Main:
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # required: button action, pandas saving, delete entries(except email)
    ui = UI()
    data_manage = DataManage(ui)
    data_manage.init_save_file()
    ui.set_add_data_btn_command(data_manage.save_data2file)


if __name__ == '__main__':
    m = Main()
    m.ui.setup_ui()
