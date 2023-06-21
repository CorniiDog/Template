[Back to DOCS.md](DOCS.md)

Import Statement: `import main`

Alternative Import Statement: `from main import *`

# >  class Test #

### [class Test:](./../main.py#L4) 

Notes

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


 <details>
<summary>

#### Functions and Classes

</summary>

# >  >  class Test.Test_Contact #

### [class Test_Contact:](./../main.py#L20) 

Notes

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


 <details>
<summary>

#### Functions and Classes

</summary>

# >  >  >  function Test.Test_Contact.init #

### [def __init__(self, phone: str, address: int):](./../main.py#L36) 

Notes

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

# >  >  >  function Test.Test_Contact.str #

### [def __str__(self):](./../main.py#L63) 

Notes

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

# >  >  function Test.init #

### [def __init__(self, name: str, age: int, contact: Test_Contact):](./../main.py#L90) 

Notes

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

# >  >  function Test.str #

### [def __str__(self):](./../main.py#L119) 

Notes

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

# >  function print_hi #

### [def print_hi(name: str) -> None:](./../main.py#L146) 

Notes

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

