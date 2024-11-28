class Node():
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
    
class LinkedList():
    def __init__(self, head=None):
        self.head = head
    
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            next_node = self.head
            while next_node.next is not None:
                next_node = next_node.next
            next_node.next = new_node
    
    def pop(self):
        if self.head is None:
            return None
        current = self.head
        if current.next is None:
            self.head = None
            return current.data
        while current.next.next is not None:
            previous = current
            current = current.next
        previous.next = None
        return current.data
    def pop(self):
        if self.head is None:
            return None
        current = self.head
        if current.next is None:
            self.head = None
            return current.data
        while current.next.next is not None:
            previous = current
            current = current.next
        previous.next = None
        return current.data

stack = LinkedList()
stack.append('A')
stack.append(10)
stack.append('abc')

current = stack.head
i = 0
while current is not None:
    print('data[{:d}]: {}'.format(i, current.data))
    current = current.next
    i += 1

print('-----------------')
while stack.head is not None:
    print('pop={}'.format(stack.pop()))