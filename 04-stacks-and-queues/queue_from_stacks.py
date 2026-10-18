class Queue:
    """FIFO queue built from two stacks. Each item moves at most once."""

    def __init__(self):
        self._in = []
        self._out = []

    def enqueue(self, item):
        self._in.append(item)

    def dequeue(self):
        if not self._out:
            while self._in:
                self._out.append(self._in.pop())
        if not self._out:
            raise IndexError("dequeue from empty queue")
        return self._out.pop()

    def __len__(self):
        return len(self._in) + len(self._out)
