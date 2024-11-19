import pandas as pd
import os.path


class DataManage:
    def __init__(self, ui, file_name='data.txt'):
        self.__data_dict = {'Website': [], 'Email/Username': [], 'Password': []}
        self.__data = None
        self.__file_name = file_name
        self.__ui = ui

    @property
    def file_name(self):
        return self.__file_name

    def load_or_init_data(self):
        if os.path.exists(self.__file_name):
            self.__load_existing_data()
        else:
            # Initialize an empty DataFrame and save it
            self.__data = pd.DataFrame(columns=['Website', 'Email/Username', 'Password'])
            self.__data.to_csv(self.__file_name, index=False, header=True)

    def __load_existing_data(self):
        # Load existing data with specified column names
        self.__data = pd.read_csv(self.__file_name, header=None,
                                  names=['Website', 'Email/Username', 'Password'])
        self.__data = self.__data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
        self.__format_data()

    def __format_data(self):
        # Generate the 'Formatted' column
        self.__data['Formatted'] = self.__data[['Website', 'Email/Username', 'Password']].astype(str).apply(
            lambda x: ' | '.join(x), axis=1)

    def save_data2file(self):
        self.gather_entry_data()
        self.__data = pd.DataFrame(self.__data_dict)
        # Save the entire DataFrame
        self.__data.to_csv(self.__file_name, mode='a', index=False, header=False)

    def gather_entry_data(self):
        self.__data_dict['Website'].append(self.__ui.website)
        self.__data_dict['Email/Username'].append(self.__ui.email)
        self.__data_dict['Password'].append(self.__ui.password)
