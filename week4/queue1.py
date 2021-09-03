from typing import Deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:  # checks if queue is empty
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node  # same as above 2 lines
        else:
            self.tail.next = new_node  # set this end value to the new node after tail
            self.tail = new_node  # make new node new tail

        self.num_nodes += 1

    def dequeue(self):
        if self.head is None:
            return None

        dequeue_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return dequeue_node_value


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue('d')
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")  # still removes value, just not 'd'
print("Pass" if (q.size() == 2) else "Fail")
