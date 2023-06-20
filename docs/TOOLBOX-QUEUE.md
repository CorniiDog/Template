[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import queue`

Alternative Import Statement: `from toolbox.queue import *`

# Queue #

### [class Queue:](./../toolbox/queue.py#L2) ###

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

# Queue.__init__ #

### [def __init__(self, queue_list: list = None, max_size: int = None):](./../toolbox/queue.py#L30) ###

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

# Queue.enqueue #

### [def enqueue(self, item):](./../toolbox/queue.py#L61) ###

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

# Queue.dequeue #

### [def dequeue(self):](./../toolbox/queue.py#L90) ###

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

# Queue.size #

### [def size(self) -> int:](./../toolbox/queue.py#L118) ###

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

# Queue.is_empty #

### [def is_empty(self) -> bool:](./../toolbox/queue.py#L146) ###

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

# Queue.peek #

### [def peek(self):](./../toolbox/queue.py#L173) ###

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

# Queue.get_list #

### [def get_list(self):](./../toolbox/queue.py#L201) ###

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

# Queue.__len__ #

### [def __len__(self):](./../toolbox/queue.py#L230) ###

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

# Queue.copy #

### [def copy(self):](./../toolbox/queue.py#L256) ###

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

# Queue.__copy__ #

### [def __copy__(self):](./../toolbox/queue.py#L288) ###

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

# Queue.__eq__ #

### [def __eq__(self, other):](./../toolbox/queue.py#L317) ###

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

# Queue.__ne__ #

### [def __ne__(self, other):](./../toolbox/queue.py#L348) ###

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

# Queue.__getitem__ #

### [def __getitem__(self, index):](./../toolbox/queue.py#L373) ###

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

# Queue.__setitem__ #

### [def __setitem__(self, index, value):](./../toolbox/queue.py#L397) ###

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

# Queue.__delitem__ #

### [def __delitem__(self, index):](./../toolbox/queue.py#L423) ###

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

# Queue.__iter__ #

### [def __iter__(self):](./../toolbox/queue.py#L447) ###

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

# Queue.__reversed__ #

### [def __reversed__(self):](./../toolbox/queue.py#L471) ###

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

# Queue.__contains__ #

### [def __contains__(self, item):](./../toolbox/queue.py#L495) ###

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

# Queue.__add__ #

### [def __add__(self, other):](./../toolbox/queue.py#L519) ###

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

# Queue.__iadd__ #

### [def __iadd__(self, other):](./../toolbox/queue.py#L550) ###

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

# Queue.__mul__ #

### [def __mul__(self, other):](./../toolbox/queue.py#L578) ###

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

# Queue.__imul__ #

### [def __imul__(self, other):](./../toolbox/queue.py#L607) ###

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

# Queue.__str__ #

### [def __str__(self):](./../toolbox/queue.py#L636) ###

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

