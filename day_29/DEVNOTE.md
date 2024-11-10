### dependency injection 
- `def __init__` should have attribute initialization only. Assigning should be later. 
- especially getting from other class 
### lambda usage: why `m.set_add_btn_command(m.save_data2file)` not working?
`add_button = tk.Button(root, text="Add", width=36, command=self.add_data_btn_command)`
- directly calls this function whether the function assigned

`add_button = tk.Button(root, text="Add", width=36, command=lamda: self.add_data_btn_command)`
- lambda works as a wrapper to prevent an immediate error 
### in pandas what is dtype and "object"?
- `self.__data = self.__data.apply(lambda x: x.str.strip() if x.dtype == "object" else x)`
- dtype in pandas is data type.
- "object" is string type
### Add button didn’t work
- `ui.set_add_data_btn_command(data_manage.save_data2file())` to this `ui.set_add_data_btn_command(data_manage.save_data2file)`
- `class UI:` Avoiding putting all code into `def __init__(self):`
### root.mainloop() only at the bottom of the main class
- it will block below lines
### garbage collection: photo image not showing. Why?
`logo_label = tk.Label(self.__root, image=logo_image) # to self.logo_image`
- with `self`, attribute will prevent garbage collection

