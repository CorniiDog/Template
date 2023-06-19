# DOCUMENTATION TABLE OF CONTENTS #

This is the documentation for the project Template.

## INSTRUCTIONS.md ##

[HOW TO INSTALL CONDA](/docs/INSTRUCTIONS.md#how-to-install-conda)

[HOW TO CREATE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#how-to-create-conda-environment)

[HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY](/docs/INSTRUCTIONS.md#how-to-connect-interpreter-to-jetbrains-gateway)

[HOW TO INSTALL REQUIREMENTS](/docs/INSTRUCTIONS.md#how-to-install-requirements)

[HOW TO INSTALL SERVICE](/docs/INSTRUCTIONS.md#how-to-install-service)

[HOW TO UNINSTALL SERVICE](/docs/INSTRUCTIONS.md#how-to-uninstall-service)

[HOW TO REMOVE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#how-to-remove-conda-environment)

# API #

## Documentation For [main.py](/docs/MAIN.md) ##

### [Test](/docs/MAIN.md#test) ###

<details><summary>Documentation For Test</summary><br>Notes

```python
    This is a test class, it is used to test the documentation generator
```

Examples

```python
    test_contact = Test.Test_Contact("123-456-7890", 1234)
    test_object = Test("Bill", 20, test_contact)
    print(test_object)
```

References

```python
    No Links
```

</details>

- [class Test:](./../main.py#L4) 



### [Test.Test_Contact](/docs/MAIN.md#testtest_contact) ###

<details><summary>Documentation For Test.Test_Contact</summary><br>Notes

```python
        This is a test class, it is used to test the documentation generator
```

Examples

```python
        test_contact = Test.Test_Contact("123-456-7890", 1234)
        print(test_contact)
```

References

```python
        No Links
```

</details>

- [class Test_Contact:](./../main.py#L20) 



### [Test.Test_Contact.__init__](/docs/MAIN.md#testtest_contact__init__) ###

<details><summary>Documentation For Test.Test_Contact.__init__</summary><br>Notes

```python
            This function is called when the object is created
```

Parameters

```python
            phone : str
                The phone number of the person to greet
            address : int
                The address of the person to greet
```

Returns

```python
            None
                This function does not return anything
```

Examples

```python
            address_object = Test.Test_Contact("123-456-7890", 1234)
```

References

```python
            No Links
```

</details>

- [def __init__(self, phone: str, address: int):](./../main.py#L36) 



### [Test.Test_Contact.__str__](/docs/MAIN.md#testtest_contact__str__) ###

<details><summary>Documentation For Test.Test_Contact.__str__</summary><br>Notes

```python
            This function is called when the object is printed
```

Parameters

```python
            None
```

Returns

```python
            str
                This function returns a string representation of the object
```

Examples

```python
            address_object = Test.Test_Contact("123-456-7890", 1234)
            print(address_object)
```

References

```python
            No Links
```

</details>

- [def __str__(self):](./../main.py#L63) 



### [Test.__init__](/docs/MAIN.md#test__init__) ###

<details><summary>Documentation For Test.__init__</summary><br>Notes

```python
        This function is called when the object is created
```

Parameters

```python
        name : str
            The name of the person to greet
        age : int
            The age of the person to greet
```

Returns

```python
        None
            This function does not return anything
```

Examples

```python
        test_object = Test("Bill", 20)
```

References

```python
        No Links
```

</details>

- [def __init__(self, name: str, age: int, contact: Test_Contact):](./../main.py#L90) 



### [Test.__str__](/docs/MAIN.md#test__str__) ###

<details><summary>Documentation For Test.__str__</summary><br>Notes

```python
        This function is called when the object is printed
```

Parameters

```python
        None
```

Returns

```python
        str
            This function returns a string representation of the object
```

Examples

```python
        test_object = Test("Bill", 20)
        print(test_object)
```

References

```python
        No Links
```

</details>

- [def __str__(self):](./../main.py#L119) 



### [print_hi](/docs/MAIN.md#print_hi) ###

<details><summary>Documentation For print_hi</summary><br>Notes

```python
        ello
```

Parameters

```python
        name : str
            The name of the person to greet
```

Returns

```python
        None
            This function does not return anything
```

Examples

```python
        print_hi('PyCharm')
```

References

```python
        https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
```

</details>

- [def print_hi(name: str) -> None:](./../main.py#L146) 



## Documentation For [toolbox/database.py](/docs/TOOLBOX-DATABASE.md) ##

### [get](/docs/TOOLBOX-DATABASE.md#get) ###

<details><summary>Documentation For get</summary><br>Notes

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
    object or None
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

</details>

- [def get(name: str) -> object | None:](./../toolbox/database.py#L9) 



### [save](/docs/TOOLBOX-DATABASE.md#save) ###

<details><summary>Documentation For save</summary><br>Notes

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

</details>

- [def save(name: str, data: any) -> None:](./../toolbox/database.py#L40) 



### [delete_database](/docs/TOOLBOX-DATABASE.md#delete_database) ###

<details><summary>Documentation For delete_database</summary><br>Notes

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
    object or None
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

</details>

- [def delete_database(name: str) -> object | None:](./../toolbox/database.py#L75) 



### [save_key](/docs/TOOLBOX-DATABASE.md#save_key) ###

<details><summary>Documentation For save_key</summary><br>Notes

```python
    This function is used to save keys in a secure location
```

Parameters

```python
    platform: str
        The name of the platform to be saved (e.g. 'google')
    key: str
        The key to be saved (e.g. '<google_api_key>')
    override: bool
        Whether or not to override the key if it already exists
```

Returns

```python
    None
        This function does not return anything
```

Examples

```python
    save_key('google', '<google_api_key>')
```

References

```python
    https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
```

</details>

- [def save_key(platform: str, key: str, override: bool = False) -> None:](./../toolbox/database.py#L113) 



### [load_key](/docs/TOOLBOX-DATABASE.md#load_key) ###

<details><summary>Documentation For load_key</summary><br>Notes

```python
        This function is used to load keys from a secure location
```

Parameters

```python
        platform: str
            The key to be loaded (e.g. '<google_api_key>')
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

</details>

- [def load_key(platform: str) -> str | None:](./../toolbox/database.py#L148) 



