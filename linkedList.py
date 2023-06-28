from node import Node
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def getIndex(self, index):
        if index < 0:
            raise IndexError("Index fuera de rango")

        current = self.head
        count = 0

        while current is not None and count < index:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Index fuera de rango")

        return current.value

    def delete(self, value):
        if self.head is None:
            raise ValueError("Lista vacía")

        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.value != value:
                current = current.next

            if current.next is None:
                raise ValueError("Valor no encontrado")

            current.next = current.next.next

