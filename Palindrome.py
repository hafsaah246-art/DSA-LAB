"""
Created on Wed Sep 17 08:54:12 2025

@author: User
"""

def is_palindrome(word):
    return word == word[::-1]
text =input("enter a string:")
print("is palindrome?",is_palindrome(text))


#%%

class Stack:
    def __init__(self):  # Correct constructor
        self.stack = []

    def push(self, item):       # Add item
        self.stack.append(item)

    def pop(self):              # Remove and return last item
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):             # See last item without removing
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):         # Check if stack is empty
        return self.stack == []
s = Stack()        # Creates an empty stack: []
s.push(1)          # Stack becomes: [1]
s.push(4)          # Stack becomes: [1, 2]
print(s.peek())    # Returns 2, top of the stack
print(s.pop())     # Removes and returns 2, stack becomes: [1]
print(s.is_empty())# Returns False, stack still has [1]
