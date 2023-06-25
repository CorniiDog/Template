[Back to DOCS.md](DOCS.md)

Import Statement: `import main`

Alternative Import Statement: `from main import *`

# >  class Test #

### [class Test:](./../main.py#L4) 

Note

```python
    This is a test class, it is used to test the documentation generator
```

Example

```python
    test_contact = Test.Test_Contact("123-456-7890", 1234)
    test_object = Test("Bill", 20, test_contact)
    print(test_object)
```

Reference

```python
    No Links
```


 <details>
<summary>

#### Functions and Classes

</summary>

# >  >  class Test.Test_Contact #

### [class Test_Contact:](./../main.py#L20) 

Note

```python
        This is a test class, it is used to test the documentation generator
```

Example

```python
        test_contact = Test.Test_Contact("123-456-7890", 1234)
        print(test_contact)
```

Reference

```python
        No Links
```


 <details>
<summary>

#### Functions and Classes

</summary>

# >  >  >  function Test.Test_Contact.init #

### [def __init__(self, phone: str, address: int):](./../main.py#L36) 

Note

```python
            This function is called when the object is created
```

Parameter

```python
            phone : str
                The phone number of the person to greet
            address : int
                The address of the person to greet
```

Return

```python
            None
                This function does not return anything
```

Example

```python
            address_object = Test.Test_Contact("123-456-7890", 1234)
```

Reference

```python
            No Links
```

# >  >  >  function Test.Test_Contact.str #

### [def __str__(self):](./../main.py#L63) 

Note

```python
            This function is called when the object is printed
```

Parameter

```python
            None
```

Return

```python
            str
                This function returns a string representation of the object
```

Example

```python
            address_object = Test.Test_Contact("123-456-7890", 1234)
            print(address_object)
```

Reference

```python
            No Links
```

</details>

# >  >  function Test.init #

### [def __init__(self, name: str, age: int, contact: Test_Contact):](./../main.py#L90) 

Note

```python
        This function is called when the object is created
```

Parameter

```python
        name : str
            The name of the person to greet
        age : int
            The age of the person to greet
```

Return

```python
        None
            This function does not return anything
```

Example

```python
        test_object = Test("Bill", 20)
```

Reference

```python
        No Links
```

# >  >  function Test.str #

### [def __str__(self):](./../main.py#L119) 

Note

```python
        This function is called when the object is printed
```

Parameter

```python
        None
```

Return

```python
        str
            This function returns a string representation of the object
```

Example

```python
        test_object = Test("Bill", 20)
        print(test_object)
```

Reference

```python
        No Links
```

</details>

# >  function print_hi #

### [def print_hi(name: str) -> None:](./../main.py#L146) 

Note

```python
        ello
```

Parameter

```python
        name : str
            The name of the person to greet
```

Return

```python
        None
            This function does not return anything
```

Example

```python
        print_hi('PyCharm')
```

Reference

```python
        https://www.jetbrains.com/help/pycharm/creating-and-running-your-first-python-project.html
```

