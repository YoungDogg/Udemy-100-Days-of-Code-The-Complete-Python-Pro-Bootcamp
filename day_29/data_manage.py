class DataManage:
    def __init__(self):
        self.__data_dict = None
        self.__data = None
        self.__file_name = 'data.txt'

    # pandas saving
    def init_save_file(self):
        if not os.path.exists(self.__file_name):
            # Create initial DataFrame
            self.__data_dict = {
                'Website': ['dummy'],
                'Email/Username': ['dummy@email.com'],
                'Password': ['qwerty']
            }
            self.__data = pd.DataFrame(self.__data_dict)
            # Generate the 'Formatted' column
            self.__data['Formatted'] = self.__data[['Website', 'Email/Username', 'Password']].astype(str).apply(
                lambda x: ' | '.join(x), axis=1)
            # Save to file
            self.__data['Formatted'].to_csv(self.__file_name, index=False, header=False)
        else:
            # Load existing data and add 'Formatted' if missing
            self.__data = pd.read_csv(self.__file_name, header=None,
                                      names=['Website', 'Email/Username', 'Password'])
            if 'Formatted' not in self.__data.columns:
                self.__data['Formatted'] = self.__data[['Website', 'Email/Username', 'Password']].astype(str).apply(
                    lambda x: ' | '.join(x), axis=1)

        # Save only the 'Formatted' column

    def save_data2file(self):
        self.gather_engtry_data()
        self.__data['Formatted'].to_csv(self.__file_name, index=False, header=False)

        # gather entry data

    def gather_engtry_data(self):
        self.__data_dict['Website'].append(website_entry.get())
        self.__data_dict['Email/Username'].append(email_entry.get())
        self.__data_dict['Password'].append(password_entry.get())

