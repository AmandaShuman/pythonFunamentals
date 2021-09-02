class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    #constructor method will auto run every time new object is instantiated in this class
    def __init__(self):  
        #  even though object doesn't exist yet, we can initialize 
        self.head = None
    
    def append(self, value):
        new_node = Node(value)

        # append to list that doesn't have any nodes in it
        if self.head is None:
            self.head = new_node
            print("Head Node created:", self.head.value)
            return
        
        # find tail node of linked list
        node = self.head
        while node.next is not None:
            node = node.next

        node.next = new_node
        print("Append new Node with value:", node.next.value)

llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")