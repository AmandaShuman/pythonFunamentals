class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # denotes lack of any value

head = Node("1st Node")
head.next = Node("2nd Node")
head.next.next = Node("3rd Node")

print(head.value)  # print 1st node
print(head.next.value)  # print 2nd node
print(head.next.next.value)  # print 3rd node