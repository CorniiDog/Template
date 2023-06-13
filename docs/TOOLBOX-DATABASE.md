Import Statement: `from toolbox import database`

Alternative Import Statement: `from toolbox.database import *`

# get #

### [def get(name: str) -> object:](./../toolbox/database.py#L8) ###

Notes

```python
    This function is used to load objects from the database folder
```

Parameters

```python
    name : str
        The name of the file to be loaded
```

Returns

```python
    object
        The object loaded from the file, could be anything
```

Examples

```python
    spreadsheet_data = get('spreadsheet_people')
```

References

```python
    No Links
```

# save #

### [def save(name: str, data: any) -> None:](./../toolbox/database.py#L39) ###

Notes

```python
    This function is used to save objects to the database folder
```

Parameters

```python
    name : str
        The name of the file to be saved
    data : any
        The data to be saved
```

Returns

```python
    None
        This function does not return anything
```

Examples

```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)
```

References

```python
    No Links
```

# delete_database #

### [def delete_database(name: str) -> object:](./../toolbox/database.py#L73) ###

Notes

```python
    This function is used to delete objects from the database folder
```

Parameters

```python
    name : str
        The name of the file to be deleted
```

Returns

```python
    object
        The object loaded from the file, could be anything
```

Examples

```python
    spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}

    save('spreadsheet_people', spreadsheet_data)

    delete_database('spreadsheet_people')
```

References

```python
    No Links
```

# save_key #

### [def save_key(platform: str, key: str, override: bool=False) -> None:](./../toolbox/database.py#L110) ###

Notes

```python
    This function is used to save keys in a secure location
```

Parameters

```python
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. 'google_api_key')
```

Returns

```python
    None
        This function does not return anything
```

Examples

```python
    save_key('google', 'google_api_key')
```

References

```python
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```

# load_key #

### [def load_key(platform: str) -> str:](./../toolbox/database.py#L143) ###

Notes

```python
        This function is used to load keys from a secure location
```

Parameters

```python
        key: str
            The key to be loaded (e.g. 'google_api_key')
```

Returns

```python
        str or None
            This function returns the key if it exists, otherwise it returns None
```

Examples

```python
        key = load_key('google')
```

References

```python
        https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```

