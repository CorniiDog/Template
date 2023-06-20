[Back to README.md](/README.md)

# DOCUMENTATION TABLE OF CONTENTS #

This is the documentation for the project Template.

## INSTRUCTIONS.md ##

[1. HOW TO INSTALL ANACONDA](/docs/INSTRUCTIONS.md#1.-how-to-install-anaconda)

[2. HOW TO CREATE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#2.-how-to-create-conda-environment)

[3. HOW TO CONNECT INTERPRETER TO JETBRAINS GATEWAY](/docs/INSTRUCTIONS.md#3.-how-to-connect-interpreter-to-jetbrains-gateway)

[4. HOW TO INSTALL REQUIREMENTS](/docs/INSTRUCTIONS.md#4.-how-to-install-requirements)

[5. HOW TO INSTALL SERVICE](/docs/INSTRUCTIONS.md#5.-how-to-install-service)

[A. HOW TO REMOVE CONDA ENVIRONMENT](/docs/INSTRUCTIONS.md#a.-how-to-remove-conda-environment)

[B.HOW TO UNINSTALL SERVICE](/docs/INSTRUCTIONS.md#b.how-to-uninstall-service)

# API #


<details>
<summary>

## Documentation For [main.py](/docs/MAIN.md)

</summary>


<details>
<summary>



### [class Test](/docs/MAIN.md#class-test) ###



</summary>

[class Test:](./../main.py#L4) 

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



</details>


<details>
<summary>



### [class Test.Test_Contact](/docs/MAIN.md#class-testtest_contact) ###



</summary>

[class Test_Contact:](./../main.py#L20) 

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



</details>


<details>
<summary>



### [function Test.Test_Contact.init](/docs/MAIN.md#function-testtest_contactinit) ###



</summary>

[def __init__(self, phone: str, address: int):](./../main.py#L36) 

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



</details>


<details>
<summary>



### [function Test.Test_Contact.str](/docs/MAIN.md#function-testtest_contactstr) ###



</summary>

[def __str__(self):](./../main.py#L63) 

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


<details>
<summary>



### [function Test.init](/docs/MAIN.md#function-testinit) ###



</summary>

[def __init__(self, name: str, age: int, contact: Test_Contact):](./../main.py#L90) 

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



</details>


<details>
<summary>



### [function Test.str](/docs/MAIN.md#function-teststr) ###



</summary>

[def __str__(self):](./../main.py#L119) 

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


<details>
<summary>



### [function print_hi](/docs/MAIN.md#function-print_hi) ###



</summary>

[def print_hi(name: str) -> None:](./../main.py#L146) 

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



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/queue.py](/docs/TOOLBOX-QUEUE.md)

</summary>


<details>
<summary>



### [class Queue](/docs/TOOLBOX-QUEUE.md#class-queue) ###



</summary>

[class Queue:](./../toolbox/queue.py#L2) 

Notes

```python
    A queue is a data structure that follows the First In First Out (FIFO) principle.
    This means that the first item added to the queue will be the first item removed from the queue.
    A queue can be implemented using a list or a linked list.
```

Examples

```python
    queue = Queue([1, 2, 3, 4, 5], 10)

    a = queue.dequeue()
    print(a)
```

References

```python
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
```



</details>


<details>
<summary>



### [function Queue.init](/docs/TOOLBOX-QUEUE.md#function-queueinit) ###



</summary>

[def __init__(self, queue_list: list = None, max_size: int = None):](./../toolbox/queue.py#L30) 

Notes

```python
        If the queue_list is not None, then the queue will be initialized with the list
        If the max_size is not None, then the queue will be initialized with the max_size
```

Returns

```python
        None
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], 10)

        a = queue.dequeue()
        print(a)
```



</details>


<details>
<summary>



### [function Queue.enqueue](/docs/TOOLBOX-QUEUE.md#function-queueenqueue) ###



</summary>

[def enqueue(self, item):](./../toolbox/queue.py#L61) 

Notes

```python
        Adds the item to the end of the queue
```

Returns

```python
        None
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        print(queue)
```



</details>


<details>
<summary>



### [function Queue.dequeue](/docs/TOOLBOX-QUEUE.md#function-queuedequeue) ###



</summary>

[def dequeue(self):](./../toolbox/queue.py#L90) 

Notes

```python
        Removes the first item from the queue
```

Returns

```python
        item: any
            The item that was removed from the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.dequeue()
        print(a)
```



</details>


<details>
<summary>



### [function Queue.size](/docs/TOOLBOX-QUEUE.md#function-queuesize) ###



</summary>

[def size(self) -> int:](./../toolbox/queue.py#L118) 

Notes

```python
        Returns the size of the queue
```

Returns

```python
        size: int
            The size of the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        print(queue.size())
```



</details>


<details>
<summary>



### [function Queue.is_empty](/docs/TOOLBOX-QUEUE.md#function-queueis_empty) ###



</summary>

[def is_empty(self) -> bool:](./../toolbox/queue.py#L146) 

Notes

```python
        Returns True if the queue is empty, False otherwise
```

Returns

```python
        is_empty: bool
            True if the queue is empty, False otherwise
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(queue.is_empty())
```



</details>


<details>
<summary>



### [function Queue.peek](/docs/TOOLBOX-QUEUE.md#function-queuepeek) ###



</summary>

[def peek(self):](./../toolbox/queue.py#L173) 

Notes

```python
        Returns the first item in the queue without removing it
```

Returns

```python
        item: any
            The first item in the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.peek()
        print(a)
```



</details>


<details>
<summary>



### [function Queue.get_list](/docs/TOOLBOX-QUEUE.md#function-queueget_list) ###



</summary>

[def get_list(self):](./../toolbox/queue.py#L201) 

Notes

```python
        Returns the list of items in the queue
```

Returns

```python
        list: list
            The list of items in the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.get_list()
        print(a)
```



</details>


<details>
<summary>



### [function Queue.len](/docs/TOOLBOX-QUEUE.md#function-queuelen) ###



</summary>

[def __len__(self):](./../toolbox/queue.py#L230) 

Notes

```python
        Returns the size of the queue
```

Returns

```python
        size: int
            The size of the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(len(queue))
```



</details>


<details>
<summary>



### [function Queue.copy](/docs/TOOLBOX-QUEUE.md#function-queuecopy) ###



</summary>

[def copy(self):](./../toolbox/queue.py#L256) 

Notes

```python
        Returns a copy of the queue
```

Returns

```python
        new_queue: Queue
            A copy of the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```



</details>


<details>
<summary>



### [function Queue.copy](/docs/TOOLBOX-QUEUE.md#function-queuecopy) ###



</summary>

[def __copy__(self):](./../toolbox/queue.py#L288) 

Notes

```python
        Returns a copy of the queue
```

Returns

```python
        new_queue: Queue
            A copy of the queue
```

Examples

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```



</details>


<details>
<summary>



### [function Queue.eq](/docs/TOOLBOX-QUEUE.md#function-queueeq) ###



</summary>

[def __eq__(self, other):](./../toolbox/queue.py#L317) 

Notes

```python
        Returns True if the queues are equal, False otherwise
```

Returns

```python
        is_equal: bool
            True if the queues are equal, False otherwise
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue == other)
```



</details>


<details>
<summary>



### [function Queue.ne](/docs/TOOLBOX-QUEUE.md#function-queuene) ###



</summary>

[def __ne__(self, other):](./../toolbox/queue.py#L348) 

Notes

```python
        Returns True if the queues are not equal, False otherwise
```

Returns

```python
        is_not_equal: bool
            True if the queues are not equal, False otherwise
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue != other)
```



</details>


<details>
<summary>



### [function Queue.getitem](/docs/TOOLBOX-QUEUE.md#function-queuegetitem) ###



</summary>

[def __getitem__(self, index):](./../toolbox/queue.py#L373) 

Notes

```python
        Returns the item at the given index
```

Returns

```python
        item: any
            The item at the given index
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue[2])
```



</details>


<details>
<summary>



### [function Queue.setitem](/docs/TOOLBOX-QUEUE.md#function-queuesetitem) ###



</summary>

[def __setitem__(self, index, value):](./../toolbox/queue.py#L397) 

Notes

```python
        Sets the item at the given index to the given value
```

Returns

```python
        None
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue[2] = 10
        print(queue)
```



</details>


<details>
<summary>



### [function Queue.delitem](/docs/TOOLBOX-QUEUE.md#function-queuedelitem) ###



</summary>

[def __delitem__(self, index):](./../toolbox/queue.py#L423) 

Notes

```python
        Deletes the item at the given index
```

Returns

```python
        None
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        del queue[2]
        print(queue)
```



</details>


<details>
<summary>



### [function Queue.iter](/docs/TOOLBOX-QUEUE.md#function-queueiter) ###



</summary>

[def __iter__(self):](./../toolbox/queue.py#L447) 

Notes

```python
        Returns an iterator for the queue
```

Returns

```python
        iter: iter
            An iterator for the queue
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in queue:
            print(item)
```



</details>


<details>
<summary>



### [function Queue.reversed](/docs/TOOLBOX-QUEUE.md#function-queuereversed) ###



</summary>

[def __reversed__(self):](./../toolbox/queue.py#L471) 

Notes

```python
        Returns an iterator for the queue in reverse order
```

Returns

```python
        reversed: iter
            An iterator for the queue in reverse order
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in reversed(queue):
            print(item)
```



</details>


<details>
<summary>



### [function Queue.contains](/docs/TOOLBOX-QUEUE.md#function-queuecontains) ###



</summary>

[def __contains__(self, item):](./../toolbox/queue.py#L495) 

Notes

```python
        Returns True if the item is in the queue, False otherwise
```

Returns

```python
        is_in: bool
            True if the item is in the queue, False otherwise
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(1 in queue)
```



</details>


<details>
<summary>



### [function Queue.add](/docs/TOOLBOX-QUEUE.md#function-queueadd) ###



</summary>

[def __add__(self, other):](./../toolbox/queue.py#L519) 

Notes

```python
        Returns a new queue with the items from both queues
```

Returns

```python
        new_queue: Queue
            A new queue with the items from both queues
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        new_queue = queue + other
        print(new_queue)
```



</details>


<details>
<summary>



### [function Queue.iadd](/docs/TOOLBOX-QUEUE.md#function-queueiadd) ###



</summary>

[def __iadd__(self, other):](./../toolbox/queue.py#L550) 

Notes

```python
        Returns this queue with the items from both queues
```

Returns

```python
        self: Queue
            This queue with the items from both queues
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        queue += other
        print(queue)
```



</details>


<details>
<summary>



### [function Queue.mul](/docs/TOOLBOX-QUEUE.md#function-queuemul) ###



</summary>

[def __mul__(self, other):](./../toolbox/queue.py#L578) 

Notes

```python
        Returns a new queue with the items from this queue repeated the given number of times
```

Returns

```python
        new_queue: Queue
            A new queue with the items from this queue repeated the given number of times
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        new_queue = queue * 3
        print(new_queue)
```



</details>


<details>
<summary>



### [function Queue.imul](/docs/TOOLBOX-QUEUE.md#function-queueimul) ###



</summary>

[def __imul__(self, other):](./../toolbox/queue.py#L607) 

Notes

```python
        Returns this queue with the items from this queue repeated the given number of times
```

Returns

```python
        self: Queue
            This queue with the items from this queue repeated the given number of times
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue *= 3
        print(queue)
```



</details>


<details>
<summary>



### [function Queue.str](/docs/TOOLBOX-QUEUE.md#function-queuestr) ###



</summary>

[def __str__(self):](./../toolbox/queue.py#L636) 

Notes

```python
        Returns a string representation of the queue
```

Returns

```python
        string: str
            A string representation of the queue
```

Examples

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue)
```



</details>

<br></details>


<details>
<summary>

## Documentation For [toolbox/database.py](/docs/TOOLBOX-DATABASE.md)

</summary>


<details>
<summary>



### [function slugify](/docs/TOOLBOX-DATABASE.md#function-slugify) ###



</summary>

[def slugify(value, allow_unicode=False):](./../toolbox/database.py#L7) 

Notes

```python
    This function is used to slugify strings, which basically means to remove all special characters and replace them with dashes.
    This is useful for creating file names from strings.
```

Parameters

```python
    value : str
        The string to be slugified
    allow_unicode : bool
        Whether or not to allow unicode characters
```

Returns

```python
    str
        The slugified string
```

Examples

```python
    a = slugify('Hello World')
```

References

```python
    https://github.com/django/django/blob/master/django/utils/text.py
```



</details>


<details>
<summary>



### [function get](/docs/TOOLBOX-DATABASE.md#function-get) ###



</summary>

[def get(name: str) -> object:](./../toolbox/database.py#L43) 

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


<details>
<summary>



### [function save](/docs/TOOLBOX-DATABASE.md#function-save) ###



</summary>

[def save(name: str, data: any) -> None:](./../toolbox/database.py#L74) 

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



</details>


<details>
<summary>



### [function delete_database](/docs/TOOLBOX-DATABASE.md#function-delete_database) ###



</summary>

[def delete_database(name: str) -> object:](./../toolbox/database.py#L109) 

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


<details>
<summary>



### [function save_key](/docs/TOOLBOX-DATABASE.md#function-save_key) ###



</summary>

[def save_key(platform: str, key: str, override: bool = False) -> None:](./../toolbox/database.py#L147) 

Notes

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


<details>
<summary>



### [function load_key](/docs/TOOLBOX-DATABASE.md#function-load_key) ###



</summary>

[def load_key(platform: str) -> str:](./../toolbox/database.py#L194) 

Notes

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

<br></details>

