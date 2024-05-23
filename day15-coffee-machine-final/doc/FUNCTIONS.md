# Functions

## make_coffee(drink_name)

**Description**: Prepares the selected drink by reducing the necessary ingredients from the resources.

**Parameters**:
- `drink_name` (str): The name of the drink to be made.

**Returns**: None

**Example**:
```python
make_coffee('latte')
```

## check_resources(resources, drink_name)

**Description**: Checks if there are enough resources to make the specified drink.

**Parameters**:
- `resources` (dict): The available resources.
- `drink_name` (str): The name of the drink.

**Returns**: bool

**Example**:
```python
is_available = check_resources(resources, 'espresso')
```

## insert_coin()

**Description**: Insert coin and sum them.

**Parameters**: None

**Returns**: int

**Example**:
```python
input_coin = insert_coin()
```

## report(money=0)

**Description**: Print current state of resources.

**Parameters**:
- `money` (int: money)

**Returns**: None

**Example**:
```python
report(money=input_coin)
```

## make_coffee(drink_name)

**Description**: Make coffee and calculate remained resources.

**Parameters**:
- `drink_name` (str)

**Returns**: None

**Example**:
```python
make_coffee(user_input)
```

