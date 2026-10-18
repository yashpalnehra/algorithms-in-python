import pytest

from linked_list import LinkedList, Node, has_cycle


def test_build_and_iterate():
    lst = LinkedList([1, 2, 3])
    assert list(lst) == [1, 2, 3]
    assert len(lst) == 3
    assert repr(lst) == "LinkedList([1, 2, 3])"


def test_push_front_and_pop_front():
    lst = LinkedList()
    lst.push_front(2)
    lst.push_front(1)
    assert lst.pop_front() == 1
    assert list(lst) == [2]
    lst.pop_front()
    with pytest.raises(IndexError):
        lst.pop_front()


def test_remove():
    lst = LinkedList([1, 2, 3, 2])
    assert lst.remove(2)
    assert list(lst) == [1, 3, 2]
    assert lst.remove(1)
    assert list(lst) == [3, 2]
    assert not lst.remove(99)
    assert len(lst) == 2


def test_reverse():
    lst = LinkedList([1, 2, 3, 4])
    lst.reverse()
    assert list(lst) == [4, 3, 2, 1]
    empty = LinkedList()
    empty.reverse()
    assert list(empty) == []


def test_middle():
    assert LinkedList([1, 2, 3]).middle() == 2
    assert LinkedList([1, 2, 3, 4]).middle() == 3
    assert LinkedList([7]).middle() == 7
    with pytest.raises(IndexError):
        LinkedList().middle()


def test_has_cycle():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next, b.next = b, c
    assert not has_cycle(a)
    c.next = b
    assert has_cycle(a)
    assert not has_cycle(None)
