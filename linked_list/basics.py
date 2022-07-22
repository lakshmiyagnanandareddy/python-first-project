"queue"
from collections import deque
print("queue:")
queue = deque()
for i in range(0, 5):
    queue.append(i)
    print(queue)
print()
for i in range(len(queue)):
    queue.popleft()
    print(queue)
print()
"stack"
print("stack:")
stack = deque()
for i in range(0, 5):
    stack.appendleft(i)
    print(stack)
print()
for i in range(len(stack)):
    stack.popleft()
    print(stack)

"""
linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingelyList():
    def __init__(self):
        self.header = None

    def print_list(self):
        printlist = self.header
        while printlist is not None:
            print(printlist.data)
            printlist = printlist.next


list = SingelyList()
list.header = Node(6)
e2 = Node(2)
e3 = Node(3)

list.header.next = e2
e2.next = e3

list.print_list()

"""
Adding from the beginning
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglelyList:
    def __init__(self):
        self.head = None

    def print_list(self):
        print_singley = self.head
        while print_singley is not None:
            print(print_singley.data)
            print_singley = print_singley.next

    def AddAtBegin(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        self.head = NewNode


list = SinglelyList()
list.head = Node(28)
e2 = Node(39)
e3 = Node(49)

list.head.next = e2
e2.next = e3

list.AddAtBegin(70)

list.print_list()

"""
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglelyList:
    def __init__(self):
        self.head = None

    def Print_list(self):
        Print_Singley = self.head
        while Print_Singley is not None:
            print(Print_Singley.data)
            Print_Singley = Print_Singley.next

    def Insert_at_the_end(self, data):
        Newnode = Node(data)
        insert = self.head
        while insert.next is not None:
            insert = insert.next
        insert.next = Newnode


list = SinglelyList()
list.head = Node(4)
E2 = Node(9)
E3 = Node(23)

list.head.next = E2
E2.next = E3

list.Insert_at_the_end(2)

list.Print_list()

"""
Insert node between two nodes
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingelyList:
    def __init__(self):
        self.head = None

    def Print_list(self):
        printSinglely = self.head
        while printSinglely is not None:
            print(printSinglely.data)
            printSinglely = printSinglely.next

    def AtBetween(self, between, data):
        NewNode = Node(data)
        NewNode.next = between.next
        between.next = NewNode


list = SingelyList()
list.head = Node(18)
E2 = Node(40)
E3 = Node(22)
E4 = Node(56)

list.head.next = E2
E2.next = E3
E3.next = E4

list.AtBetween(E2, 44)

list.Print_list()


"""
Remove a node
"""

print()
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingelyList:
    def __init__(self):
        self.head = None

    def Print_list(self):
        print_singely = self.head
        while print_singely is not None:
            print(print_singely.data)
            print_singely = print_singely.next

    def RemoveNode(self, Remove):
        HeadVal = self.head
        if HeadVal.data == Remove:
            self.head = HeadVal.next
            return
        while HeadVal is not None :
            if HeadVal.data == Remove:
                break
            prev = HeadVal
            HeadVal = HeadVal.next
        prev.next = HeadVal.next




list = SingelyList()
list.head = Node(33)
E2 = Node(43)
E3 = Node(22)
E4 = Node(11)

list.head.next = E2
E2.next = E3
E3.next = E4

list.RemoveNode(33)

list.Print_list()

print()
"""
Doubly_Linked_list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class doubly:
    def __init__(self):
        self.head = None

    def add(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def Print_List(self):
        Print_list = self.head
        while Print_list is not None:
            print(Print_list.data)
            last = Print_list
            Print_list = Print_list.next


list = doubly()
list.add(19)
list.add(33)
list.add(23)
list.Print_List()

print()
"""
Doubly link list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.head = None

    def push(self, node):
        NewNode = Node(node)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def insert(self, prev, data):
        NewNode = Node(data)
        NewNode.next = prev.next
        prev.next = NewNode
        NewNode.prev = prev
        if NewNode.next is not None:
            NewNode.next.prev = NewNode

    def Print_List(self):
        PrintDoubly = self.head
        while PrintDoubly is not None:
            print(PrintDoubly.data)
            prev = PrintDoubly
            PrintDoubly = PrintDoubly.next


list = Doubly()
list.push(23)
list.push(34)
list.push(33)
list.insert(list.head.next, 42)
list.Print_List()

"""
Append in doubly linked list.
"""
print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Doubly:
    def __init__(self):
        self.head = None

    def push(self, data):
        NewNode = Node(data)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode

    def append(self, data):
        last = self.head
        NewNode = Node(data)
        while last.next is not None:
            last = last.next
        NewNode.prev = last
        last.next = NewNode

    def print_list(self):
        Print_doubly = self.head
        while Print_doubly is not None:
            print(Print_doubly.data)
            prev = Print_doubly
            Print_doubly = Print_doubly.next

    def print_reverse(self):
        last = self.head
        while last.next is not None:
            last = last.next
        while last is not None:
            print(last.data)
            last = last.prev


list = Doubly()
list.push(23)
list.push(44)
list.push(14)
list.append(88)
list.print_list()
print()
list.print_reverse()