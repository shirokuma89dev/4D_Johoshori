from linked_list import LinkedList
from linked_list import Node

def ordering(linked_list):
    sorted_list = LinkedList()  # 昇順にデータを格納する新しいリストを作成
    current = linked_list.head  # 元のリストの先頭から開始

    while current is not None:
        data = current.data
        if sorted_list.head is None or data < sorted_list.head.data:
            # 新しいリストが空か、先頭より小さい場合は先頭に追加
            sorted_list.head = Node(data, sorted_list.head)
        else:
            # 適切な位置を探して挿入
            sorted_current = sorted_list.head
            while sorted_current.next is not None and sorted_current.next.data < data:
                sorted_current = sorted_current.next
            sorted_current.next = Node(data, sorted_current.next)
        current = current.next

    linked_list.head = sorted_list.head  # 元のリストの先頭を更新


original_list = LinkedList()
original_list.append(3)
original_list.append(1)
original_list.append(4)
original_list.append(2)

print("Before ordering:")
current = original_list.head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("End of list")

ordering(original_list)

print("After ordering:")
current = original_list.head
while current is not None:
    print(current.data, end=" -> ")
    current = current.next
print("End of list")
