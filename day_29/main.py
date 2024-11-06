import tkinter as tk
import pandas as pd
import os.path
from ui import UI
from data_manage import DataManage

class Main:
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    # ---------------------------- SAVE PASSWORD ------------------------------- #
    # if saved, delete entries except Email
    # required: button action, pandas saving, delete entries
    # button action

    ui = UI()
    data_manage = DataManage()
    data_manage.init_save_file()
    data_manage.set_add_btn_command(data_manage.save_data2file())


if __name__ == '__main__':
    m = Main()

