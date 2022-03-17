import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class ShiftList:
    def right_on(self):
        self.head = self.head.prev

    def left_on(self):
        self.head = self.head.next

    length = 0

    def __init__(self):
        self.head = None

    def append(self, data):
        if self.head is None:
            newNode = Node(data)
            newNode.prev = None
            self.head = newNode

        elif self.length == 1:
            newNode = Node(data)
            newNode.next = self.head
            newNode.prev = self.head
            self.head.next = newNode
            self.head.prev = newNode

        else:
            newNode = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.prev = cur
            newNode.next = self.head
            self.head.prev = newNode
        self.length += 1

    def print(self):
        cur = self.head
        while cur.next != self.head:
            print(cur.data)
            cur = cur.next
        print(cur.data)

    def pop(self, n):
        count = 0
        cur = self.head

        while count != n:
            cur = cur.next
            n += 1

        cur.prev.next = cur.next
        cur.next.prev = cur.prev

        return cur.data


shiftlist = ShiftList()
shiftlist.append(35)
shiftlist.append(1)
shiftlist.append(65)
shiftlist.append(random.randint(1,100))
shiftlist.append(55)
shiftlist.append(55)
shiftlist.print()
shiftlist.right_on()
shiftlist.print()
shiftlist.right_on()
shiftlist.print()
