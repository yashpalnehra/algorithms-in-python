class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, values=()):
        self.head = None
        self.size = 0
        for value in values:
            self.append(value)

    def push_front(self, value):
        self.head = Node(value, self.head)
        self.size += 1

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
        self.size += 1

    def pop_front(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return value

    def remove(self, value):
        """Remove the first node holding value. Returns True if one was found."""
        prev = None
        node = self.head
        while node:
            if node.value == value:
                if prev is None:
                    self.head = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True
            prev, node = node, node.next
        return False

    def reverse(self):
        prev = None
        node = self.head
        while node:
            node.next, prev, node = prev, node, node.next
        self.head = prev

    def middle(self):
        """Value in the middle, the second of the two for even lengths."""
        if self.head is None:
            raise IndexError("middle of empty list")
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __len__(self):
        return self.size

    def __repr__(self):
        return "LinkedList([" + ", ".join(repr(v) for v in self) + "])"


def has_cycle(head):
    """Floyd's tortoise and hare on a raw chain of nodes."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
