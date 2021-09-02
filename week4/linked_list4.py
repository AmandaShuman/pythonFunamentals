class DoubleNode:
    def __init__(self, value):
        # key characteristics is that it can hold some value
        self.value = value
        self.next = None
        self.prev = None

# when first instantiated, list won't contain any nodes
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DoubleNode(value)

        # checking if list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print("Head Node created:", self.head.value)
            return
        
        #if list is not empty and there is a head
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        print("Appended new Node with value:", self.tail.value)

dllist = DoublyLinkedList()
dllist.append("First Node")