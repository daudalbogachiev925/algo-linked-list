"""Связные списки: все виды."""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        self.size += 1

    def prepend(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
        self.size += 1

    def remove(self, data):
        cur = self.head
        prev = None
        while cur:
            if cur.data == data:
                if prev:
                    prev.next = cur.next
                else:
                    self.head = cur.next
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def reverse(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new = Node(data)
        if not self.head:
            self.head = self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.size += 1

    def to_list(self):
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def to_list_reverse(self):
        result = []
        cur = self.tail
        while cur:
            result.append(cur.data)
            cur = cur.prev
        return result

if __name__ == "__main__":
    sll = SinglyLinkedList()
    for x in [1, 2, 3, 4]:
        sll.append(x)
    print("SLL:", sll.to_list())
    sll.reverse()
    print("Reversed:", sll.to_list())

    dll = DoublyLinkedList()
    for x in [10, 20, 30]:
        dll.append(x)
    print("DLL:", dll.to_list())
    print("DLL reverse:", dll.to_list_reverse())
