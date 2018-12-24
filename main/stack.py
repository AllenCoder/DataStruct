class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, top=None):
        self.top = top

    def is__empty(self):
        return self.top is None

    def push(selfs, val):
        if selfs.is__empty():
            return
        else:
            node = StackNode(val)
            node.next = selfs.top.next
            selfs.top = node
            return

    def pop(self):
        if self.is__empty():
            raise ("Stack Data is Empty\n")
            return
        node = self.top
        self.top = self.top.next
        return node
