"""
-------------------------------------------------------
CP164 
-------------------------------------------------------
Author:  Gurkarman Reen
ID:      169030008
Email:   reen0008@mylaurier.ca
__updated__ = "2023-02-10"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List
from Movie import Movie


# Constants

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while source != []:
        stack.push(source.pop())

    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not stack.is_empty():
        target.insert(0, stack.pop())

    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    stack = Stack()
    if len(source) == 0:
        print("not valid source")
    else:
        for i in source:
            stack.push(i)
        print(f"Is it empty: {stack.is_empty()}")
        print(f"push: {stack.push(i)}")
        print(f"pop: \n{stack.pop()}")
        print(f"peek:\n{stack.peek()}")

    return


def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        queue.insert(source.pop(0))


def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not queue.is_empty():
        target.append(queue.remove())


def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    if len(a) == 0:
        print("not valid")
    else:
        for i in a:
            q.insert(i)
        print(f"Is it empty: {q.is_empty()}")
        print(f"target: {q.insert(i)}")
        print(f"remove: \n{q.remove()}")
        print(f"peek:\n{q.peek()}")

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while source != []:
        pq.insert(source.pop(0))


def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while not pq.is_empty():
        target.append(pq.remove())


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()

    if len(a) == 0:
        print("not valid")
    else:
        for i in a:
            pq.insert(i)
        print(f"Is it empty: {pq.is_empty()}")
        print(f"insert: {pq.insert(i)}")
        print(f"remove: \n{pq.remove()}")
        print(f"peek:\n{pq.peek()}")

    # tests for the priority queue methods go here
    # print the results of the method calls and verify by hand

    return


def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while source != []:
        llist.append(source.pop(0))

    return


def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not llist.is_empty():
        target.append(llist.pop(0))

    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    for i in source:
        lst.append(i)
    print(f"Is it empty: {lst.is_empty()}")
    print(f"count: {lst.count(i)}")
    key = lst[0]
    print(f"index: \n{lst.index(key)}")
    print()

    print(f"max:\n{lst.max()}")
    print()
    print(f"min:\n{lst.min()}")
    print()
    print(f"insert: {lst.insert(3, key)}")
    print()
    print(f"remove: \n{lst.remove(key)}")
    print()
    print(f"find: \n{lst.find(key)}")

    print()

    for i in lst:
        print(i)
        print()

    # tests for the List methods go here
    # print the results of the method calls and verify by hand

    return
