from day_30.json_controller import JSONData


class DataManage:
    def __init__(self, ui, file_name='data.json'):
        self.__data_dict = {'Website': [], 'Email/Username': [], 'Password': []}
        self.__file_name = file_name
        self.__ui = ui
        self.__json_handler = JSONData(self.__file_name)

    def load_or_init_data(self):
        # Check if JSON file exists; if not, create an empty one
        try:
            data = self.__json_handler.read()
            if data.empty:
                self.__json_handler.create(self.__data_dict)
        except FileNotFoundError:
            self.__json_handler.create(self.__data_dict)

    def save_data2file(self):
        # Gather user entry data and save it to the JSON file
        self.gather_entry_data()
        # Read existing data as a dictionary
        existing_data = self.__json_handler.read().to_dict(orient="list")
        print(f"existing_data:{existing_data}")

        # Append new data to the existing data
        for key in self.__data_dict:
            if key in existing_data:
                existing_data[key].extend(self.__data_dict[key])
            else:
                existing_data[key] = self.__data_dict[key]

        # Write the updated dictionary back to the JSON file
        self.__json_handler.create(existing_data)

    def gather_entry_data(self):
        self.__data_dict['Website'].append(self.__ui.website)
        self.__data_dict['Email/Username'].append(self.__ui.email)
        self.__data_dict['Password'].append(self.__ui.password)
