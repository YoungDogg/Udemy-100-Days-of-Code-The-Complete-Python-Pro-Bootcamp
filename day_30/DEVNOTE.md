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
- [x] implement to my code~~~~
  - [x] make json CRUD class
    - [x] make exception
## Search website
- [x] search class
- [x] combine with UI
# Struggled
- relative path solved linking assigning from other directory main class
## `orient`  
- `existing_data = self.__json_handler.read().to_dict(orient="list")`

### Sample DataFrame
```python
df = pd.DataFrame({
    'Website': ['example.com', 'another.com'],
    'Email/Username': ['user1@example.com', 'user2@example.com'],
    'Password': ['password123', 'securePass456']
})
```

### Results for Different `orient` Options

#### `orient='dict'` (default)
Nested dictionaries: columns are keys, values are dictionaries with index-value pairs.

```json
{
    "Website": {0: "example.com", 1: "another.com"},
    "Email/Username": {0: "user1@example.com", 1: "user2@example.com"},
    "Password": {0: "password123", 1: "securePass456"}
}
```

---

#### `orient='list'`, if to_json(), then `orient='columns'` 
Columns are keys, values are lists of all entries in that column.

```json
{
    "Website": ["example.com", "another.com"],
    "Email/Username": ["user1@example.com", "user2@example.com"],
    "Password": ["password123", "securePass456"]
}
```

---

#### `orient='records'`
Each row is converted into a dictionary; the result is a list of dictionaries.

```json
[
    {"Website": "example.com", "Email/Username": "user1@example.com", "Password": "password123"},
    {"Website": "another.com", "Email/Username": "user2@example.com", "Password": "securePass456"}
]
```

---

#### `orient='index'`
Index becomes the key, and each row's data is represented as a dictionary.

```json
{
    0: {"Website": "example.com", "Email/Username": "user1@example.com", "Password": "password123"},
    1: {"Website": "another.com", "Email/Username": "user2@example.com", "Password": "securePass456"}
}
```

---

#### `orient='split'`
Provides a dictionary with separate keys for `index`, `columns`, and `data`.

```json
{
    "index": [0, 1],
    "columns": ["Website", "Email/Username", "Password"],
    "data": [
        ["example.com", "user1@example.com", "password123"],
        ["another.com", "user2@example.com", "securePass456"]
    ]
}
```

---

### Summary Table of Use Cases

| **Orient**     | **Structure**            | **When to Use**                                                        |
|-----------------|--------------------------|-------------------------------------------------------------------------|
| `dict`         | Column-to-index mappings | Default; good for column-based access.                                 |
| `list`         | Column-to-list mappings  | Ideal for column-wise operations and appending lists.                  |
| `records`      | List of row dictionaries | Best for row-wise operations (e.g., sending JSON to an API).           |
| `index`        | Index-to-row mappings    | Useful if the index is meaningful (e.g., primary keys).                |
| `split`        | Separated metadata       | Useful for transmitting metadata like `index` and `columns` with data. |

## sticky
```python
add_button.grid(row=4, column=1, columnspan=2, pady=(10, 20), padx=(0, 20), sticky="w")
```
- "w": Aligns the widget to the west (left) side of the cell.
- "e": Aligns the widget to the east (right) side of the cell.
