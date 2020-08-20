"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 
1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


# class Stack: #Array-based implementation
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)
#         #return ?

#     def pop(self):
#         self.size = len(self.storage)
#         if self.size == 0:
#             top = None
#         else:
#             top = self.storage[self.size-1]
#             self.storage.pop(self.size-1)
#             self.size -= 1
#         return top

from singly_linked_list import LinkedList


class Stack:  # LL-based implementation
    # New elements added to head, popped off of head
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        if self.size == 0:  # self.storage.head is None and self.storage.tail is None:
            return None
        else:
            self.size -= 1
            return self.storage.remove_head()
