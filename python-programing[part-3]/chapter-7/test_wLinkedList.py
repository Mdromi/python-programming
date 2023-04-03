# python3 chapter-7/test_wLinkedList.py
# pytest chapter-7/test_wLinkedList.py

from  wLinkedList import *

def test_append():
    dll = DoublyLinkedList()

    assert dll.head.next == None, "linked list is empty, so head should point to none"

    item = 5
    dll.append(item)
    second_item = 8
    dll.append(second_item)
    assert dll.head.next.data == item, "head should point the first node"

    first_node = dll.head.next
    second_node = first_node.next
    assert first_node.next.data == second_item, 'first node should point to second node'
    assert second_node.prev.data == item, 'previous node of second_node should be the first node'
    assert str(dll) == '5, 8', 'string representation of dill should match 5,8'

def test_prepend():
    dll = DoublyLinkedList() 

    assert dll.head.next == None, 'Linked list empty, so head should point to none'

    item = 5
    dll.prepend(item)
    assert dll.head.next.data == item, 'head should point to the first node'

    new_node = dll.head.next
    old_node = new_node.next
    assert new_node.prev == None, 'previous node of the old_node should be none'
    assert old_node.prev == new_node, 'previould node of the old_node should be new_node'
    assert old_node.data == item, 'checking the data of old_node'
    assert str(dll) == '10, 5', 'string representation of dll should match 10, 5'

def test_search():
    dll = DoublyLinkedList()

    item = 5
    assert dll.search(item) == None, "item shouldn't be found in an empty list"
    dll.append(item)
    node = dll.search(item)
    assert node.data == item, "item should be found in the list"

    dll.append(10)
    dll.append(15)
    node = dll.search(10)
    assert node.data == 10, '10 should be found in the list'

    node = dll.search(20)
    assert node == None, '20 should not be found in the node'

def test_remove_node():
    dll = DoublyLinkedList()
    dll.append(5)
    node = dll.search(5)
    assert dll.head.next == node, 'head should point to node'
    dll.remove_node(node)
    assert dll.head.next == None, 'head should point to none, as list is empty'

def test_remove():
    dll = DoublyLinkedList()
    dll.append(5)
    dll.append(10)
    dll.append(15)
    dll.append(20)

    node_5 = dll.search(5)
    node_10 = dll.search(10)
    node_15 = dll.search(15)
    node_20 = dll.search(20)

    assert node_10.next == node_15
    assert node_15.prev == node_10

    # remove from middle
    dll.remove(15)
    assert node_10.next == node_20, 'now next of 10 should be 20'
    assert node_15.prev == node_10, 'now prev of 20 should be 10'
    assert str(dll) == '5,10,20', '15 should sot be in the list anymore'

    # remove from end
    dll.remove(5)
    assert dll.head.next == node_10, 'now head should point to 10'
    assert node_10.prev == None, '10 is the first node, so prev should be None'
    assert str(dll) == '10', 'dll should only contain 10'