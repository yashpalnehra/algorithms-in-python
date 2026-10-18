import pytest

from brackets import evaluate_rpn, is_balanced
from queue_from_stacks import Queue
from stack import MinStack, Stack


def test_stack_order():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.peek() == 2
    assert s.pop() == 2
    assert s.pop() == 1
    assert not s


def test_stack_empty_errors():
    with pytest.raises(IndexError):
        Stack().pop()
    with pytest.raises(IndexError):
        Stack().peek()


def test_min_stack():
    s = MinStack()
    for value in (5, 3, 7, 3, 1):
        s.push(value)
    assert s.minimum() == 1
    s.pop()
    assert s.minimum() == 3
    s.pop()
    s.pop()
    assert s.minimum() == 3
    s.pop()
    assert s.minimum() == 5


def test_queue_is_fifo():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert q.dequeue() == "a"
    q.enqueue("c")
    assert q.dequeue() == "b"
    assert q.dequeue() == "c"
    assert len(q) == 0
    with pytest.raises(IndexError):
        q.dequeue()


def test_is_balanced():
    assert is_balanced("([]{})")
    assert is_balanced("")
    assert is_balanced("a(b[c]d)e")
    assert not is_balanced("(]")
    assert not is_balanced("((")
    assert not is_balanced("))")


def test_evaluate_rpn():
    assert evaluate_rpn(["2", "3", "+", "4", "*"]) == 20
    assert evaluate_rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14
    assert evaluate_rpn(["7", "2", "/"]) == 3.5
    with pytest.raises(ValueError):
        evaluate_rpn(["1", "2"])
