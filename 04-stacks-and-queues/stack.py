class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if not self._items:
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)


class MinStack(Stack):
    """A stack that also knows its smallest item in O(1)."""

    def __init__(self):
        super().__init__()
        self._mins = []

    def push(self, item):
        super().push(item)
        # keep the running minimum next to each item
        self._mins.append(min(item, self._mins[-1]) if self._mins else item)

    def pop(self):
        self._mins.pop()
        return super().pop()

    def minimum(self):
        if not self._mins:
            raise IndexError("minimum of empty stack")
        return self._mins[-1]
