[get](#get)

#[get](toolbox/database.py#8)

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
    >>> spreadsheet_data = get('spreadsheet_people')
```

References

```python
    No Links
```

[save](#save)

#[save](toolbox/database.py#39)

Notes

```python
    This function is used to save objects to the databse folder
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
    >>> spreadsheet_data = {"People": ["Bill", "Kent", "Steve"], "Ages": [20, 30, 40]}
    >>> save('spreadsheet_people', spreadsheet_data)
```

References

```python
    No Links
```

