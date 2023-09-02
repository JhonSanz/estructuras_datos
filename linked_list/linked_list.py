
class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self, data=None):
        self.head = None
        self.tail = None
        self.size = 0

        if data is not None:
            for item in data:
                self.push_back(item)
    
    def __str__(self):
        return self.print()
    
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node.data
            node = node.next

    def push_back(self, data):
        node = self.Node(data)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.size += 1
    
    def push_front(self, data):
        node = self.Node(data)
        if self.head is None:
            self.tail = node
        else:
            node.next = self.head
        self.head = node
        self.size += 1
    
    def find(self, data):
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        return None
    
    def reverse(self):
        prev = None
        node = self.head
        while node is not None:
            next = node.next
            node.next = prev
            prev = node
            node = next
        self.head = prev

    def print(self):
        as_string = ""
        node = self.head
        while node is not None:
            as_string += str(node.data) + (", " if node.next is not None else "")
            node = node.next
        return f"[{as_string}]"

    def delete(self, data):
        prev = None
        node = self.head
        while node is not None:
            if node.data == data:
                if prev is None:
                    self.head = node.next
                else:
                    prev.next = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

my_list = LinkedList([1,2,3,4,5])
