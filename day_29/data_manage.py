import pandas as pd
import os.path


class DataManage:
    def __init__(self, ui):
        self.__data_dict = {'Website': [], 'Email/Username': [], 'Password': []}
        self.__data = None
        self.__file_name = 'data.txt'
        self.__ui = ui

        # pandas saving

    def load_or_init_data(self):
        if os.path.exists(self.__file_name):
            print('load_or_init_data true')
            self.__load_existing_data()
        else:
            self.__data = pd.DataFrame(columns=['Website', 'Email/Username', 'Password'])
            self.__data.to_csv(self.__file_name, index=False, header=False)

    def __load_existing_data(self):
        # Load existing data and add 'Formatted' if missing
        self.__data = pd.read_csv(self.__file_name, header=None,
                                  names=['Website', 'Email/Username', 'Password'])
        self.__data = self.__data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        if 'Formatted' not in self.__data.columns:
            self.__format_data()

    def __format_data(self):
        # Generate the 'Formatted' column
        self.__data['Formatted'] = self.__data[['Website', 'Email/Username', 'Password']].astype(str).apply(
            lambda x: ' | '.join(x), axis=1)

    def save_data2file(self):
        self.gather_engtry_data()
        self.__data = pd.DataFrame(self.__data_dict)
        self.__format_data()
        self.__data['Formatted'].to_csv(self.__file_name, mode='a', index=False, header=False)

    def gather_engtry_data(self):
        self.__data_dict['Website'].append(self.__ui.website)
        self.__data_dict['Email/Username'].append(self.__ui.email)
        self.__data_dict['Password'].append(self.__ui.password)
