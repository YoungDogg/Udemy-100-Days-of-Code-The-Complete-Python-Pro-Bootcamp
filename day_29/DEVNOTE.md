### How to only save 'formatted'?
    self.__data['Formatted'].to_csv(something)
### How to get entry data?
	entry.get()
### fill self.__data_dict using them	
	self.__data_dict['Website']:  entry.get()
	self.__data_dict['somthing']: otherentry.get()
### how to append to the existing save file?
    def gather_engtry_data(self):
        self.__data_dict['Website'].append(website_entry.get())
        self.__data_dict['Email/Username'].append(email_entry.get())
        self.__data_dict['Password'].append(password_entry.get())
### why `m.set_add_btn_command(m.save_data2file)` not working?
`add_button = tk.Button(root, text="Add", width=36, command=self.add_data_btn_command)`
- directly calls this function whether the function assigned

`add_button = tk.Button(root, text="Add", width=36, command=lamda: self.add_data_btn_command)`
- lambda works as a wrapper to prevent an immediate error 
### what is dtype and "object"?
- `self.__data = self.__data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)`
- dtype in pandas is data type.
- "object" is string type
### Add button didn’t work
- `ui.set_add_data_btn_command(data_manage.save_data2file())` to this `ui.set_add_data_btn_command(data_manage.save_data2file)`
- `class UI:` Avoiding putting all code into `def __init__(self):`
