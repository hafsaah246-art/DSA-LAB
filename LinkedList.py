class Node:
    def __init__(self, item, next=None):
        # assign values to instance attributes
        self.item = item
        self.next = next
class SLList:
    def __init__(self):
        # create a sentinel node with no data (item=None)
        self.sentinel = Node(None)
        # initialize length to zero
        self.length = 0
    def insert_first(self, item):
        # Insert new node right after sentinel
        new_node = Node(item, self.sentinel.next)
        self.sentinel.next = new_node
        self.length += 1
    def insert_last(self, item):
        # Traverse to the last node
        current = self.sentinel
        while current.next is not None:
            current = current.next
        # Append new node at the end
        current.next = Node(item)
        self.length += 1
    def get_first(self):
        # Return item of first node (after sentinel) or None if empty
        if self.sentinel.next is None:
            return None
        return self.sentinel.next.item

    def __len__(self):
        # Return length of list
        return self.length
l = SLList()
print(len(l))        # Output: 0
print(l.get_first()) # Output: None

l.insert_first(10)
print(len(l))        # Output: 1
print(l.get_first()) # Output: 10

l.insert_last(20)
print(len(l))        # Output: 2
print(l.get_first()) # Output: 10


#%%

def insert_at(self, i, item):
    if i < 0:
        i = 0
    p = self.sentinel
    for _ in range(i):
        if p.next is None:
            break
        p = p.next
    new_node = Node(item, p.next)
    p.next = new_node
    self.length += 1

    
#%%
from sllist import SLList   # assuming your linked list code is in sllist.py

# create an empty list
lst = SLList()

# test insertFirst
lst.insertFirst(10)
assert lst.size == 1
assert lst.sentinel.next.item == 10

# test insertLast
lst.insertLast(20)
assert lst.size == 2
assert lst.sentinel.next.next.item == 20

# test insertAt
lst.insertAt(1, 15)  # insert in the middle
assert lst.size == 3
assert lst.sentinel.next.next.item == 15

# test insertAt at front
lst.insertAt(0, 5)
assert lst.size == 4
assert lst.sentinel.next.item == 5

# test insertAt at end
lst.insertAt(10, 30)  # bigger than size → should append at end
assert lst.size == 5

# print result (for manual check)
p = lst.sentinel.next
while p is not None:
    print(p.item, end=" -> ")
    p = p.next
print("None")
