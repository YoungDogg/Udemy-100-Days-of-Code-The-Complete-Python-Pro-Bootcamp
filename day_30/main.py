from day_29.ui import UI
from day_29.password_generator import PasswordGenerator
from day_29.data_manage import DataManage
from day_29.store_to_clipboard import Clipboard
from day_30.search_website import SearchWebsite
from json_controller import JSONData


class Main:
    """Upgrade Day29 project with json data format, and search function"""

    def __init__(self):
        """Initializes the main application components."""
        self.file_name = "data.json"
        self.ui = UI()
        self.password_generator = PasswordGenerator()
        self.data_manager = DataManage(self.ui, file_name=self.file_name)
        self.clipboard = Clipboard(self.ui)
        self.json_data = JSONData(file_name=self.file_name)
        self.search_website = SearchWebsite(self.json_data, self.file_name)
        self._initialize_data()
        self._set_commands()

    def _initialize_data(self):
        """Loads or initializes data required for the application."""
        try:
            self.data_manager.load_or_init_data()
        except Exception as e:
            print(f"Error loading data: {e}")

    def _set_commands(self):
        """Binds UI buttons to their respective commands."""
        self.ui.set_add_data_command(self.data_manager.save_data2file)
        self.ui.set_generate_password_command(self.password_generator.generate_pwd)
        self.ui.set_clipboard(self.clipboard)
        self.ui.set_search_website_command(self.search_website.search_website)


if __name__ == '__main__':
    main_app = Main()
    main_app.ui.root.mainloop()
