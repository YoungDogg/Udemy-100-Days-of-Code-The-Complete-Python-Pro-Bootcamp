# Learning Goal
## Error exception
- FileNotFound
- KeyError
- IndexError
- IndexError
- TypeError
## JSON
### update
`data_file.to_json(self.file, orient="records")`
- `orient="records"` saves data format as json
### delete
  `data_file = data_file[data_file[condition_col] != condition_val]`

  `data_file.to_json(self.file, orient="records")`
- save except `condition_val`
# Coding Goal
## Make Error Handling from day_26
- [x] make day_26 main.py as class
- [x] make error handling class in day_30
## Change save data format as JSON
- [x] learn pandas json
- [ ] implement to my code
  - [x] make json CRUD class
    - [x] make exception
# Struggled
- relative path solved linking assigning from other directory main class