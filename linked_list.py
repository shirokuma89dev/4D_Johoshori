class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
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

    def insert(self, target_data, new_data):
        current = self.head
        while current is not None:
            if current.data == target_data:
                new_node = Node(new_data, current.next)
                current.next = new_node
                return
            current = current.next
        print(f"Error: {target_data}が見つかりません")

    def delete(self, target_data):
        current = self.head
        previous = None
        while current is not None:
            if current.data == target_data:
                if previous is None:  # 最初のノードを削除
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next
        print(f"Error: {target_data}が見つかりません")

    def concat(self, other_list):
        if self.head is None:
            self.head = other_list.head
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = other_list.head

    def search(self, target_data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == target_data:
                return index
            current = current.next
            index += 1
        return -1
