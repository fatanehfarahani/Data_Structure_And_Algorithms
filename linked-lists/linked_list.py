class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        self.head = Node(value, self.head)

    def to_list(self):
        result = []
        current = self.head

        while current is not None:
            result.append(current.value)
            current = current.next

        return result

    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following

        self.head = previous
