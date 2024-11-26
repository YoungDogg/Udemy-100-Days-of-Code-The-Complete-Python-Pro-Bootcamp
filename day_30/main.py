from day_26.NatoAlphabet import NatoAlphabet
from error_handle import NatoAlphabetErrorHandle

from json_controller import JSONData
from day_29.ui import UI
from day_29.password_generator import PasswordGenerator
from day_29.data_manage import DataManage
from day_29.store_to_clipboard import Clipboard
from day_30.search_website import SearchWebsite

class Main:
    def __init__(self):
        # day26
        # self.n_alphabet = NatoAlphabet()
        # self.e_handle = NatoAlphabetErrorHandle()

        # day29
        self.jsonData = None
        self.ui = UI()
        self.pwd = PasswordGenerator()
        self.data_manage = None
        self.clipboard = None
        self.file_name = "data.json"
        self.searchWebsite = None

    def set_up(self):
        # def set_class(self):
        self.ui.setup_ui()

        self.data_manage = DataManage(self.ui, file_name=self.file_name)
        self.clipboard = Clipboard(self.ui)

        self.jsonData = JSONData(file_name=self.file_name)
        self.data_manage.load_or_init_data()

        self.searchWebsite = SearchWebsite(self.jsonData, self.file_name)

        # def set_function(self):
        self.ui.set_add_data_btn_command(self.data_manage.save_data2file)
        self.ui.set_generate_pswd_btn_command(self.pwd.generate_pwd)
        self.ui.set_clipboard(self.clipboard)
        self.ui.set_search_website_btn_command(self.searchWebsite.search_website)


if __name__ == '__main__':
    # ========day26========
    # m = Main()
    # m.n_alphabet.setup()
    # word = m.e_handle.check_input_error()
    # result = m.n_alphabet.result(word)
    # print(result)

    # ========day29========
    m = Main()
    m.set_up()
    m.ui.root.mainloop()
