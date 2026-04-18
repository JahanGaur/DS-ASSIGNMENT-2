# ldst_toolkit.py

Name: Jahan Gaur
Roll No: 2501730484
Course: B.Tech CSE AI/ML
Section: G



# -----------------------------

# 1. Dynamic Array

# -----------------------------

class DynamicArray:
def **init**(self):
self.capacity = 2
self.size = 0
self.arr = [None] * self.capacity

```
def append(self, x):
    if self.size == self.capacity:
        self._resize()
    self.arr[self.size] = x
    self.size += 1

def _resize(self):
    print(f"Resizing from {self.capacity} to {self.capacity * 2}")
    self.capacity *= 2
    new_arr = [None] * self.capacity

    for i in range(self.size):
        new_arr[i] = self.arr[i]

    self.arr = new_arr

def pop(self):
    if self.size == 0:
        print("Array is empty")
        return None
    val = self.arr[self.size - 1]
    self.size -= 1
    return val

def display(self):
    print("Array:", self.arr[:self.size], "| Size:", self.size, "| Capacity:", self.capacity)
```

# -----------------------------

# 2. Singly Linked List

# -----------------------------

class Node:
def **init**(self, data):
self.data = data
self.next = None

class SinglyLinkedList:
def **init**(self):
self.head = None

```
def insert_beginning(self, x):
    new = Node(x)
    new.next = self.head
    self.head = new

def insert_end(self, x):
    new = Node(x)
    if not self.head:
        self.head = new
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new

def delete(self, x):
    temp = self.head

    if temp and temp.data == x:
        self.head = temp.next
        return

    prev = None
    while temp and temp.data != x:
        prev = temp
        temp = temp.next

    if temp:
        prev.next = temp.next
    else:
        print("Value not found")

def traverse(self):
    temp = self.head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")
```

# -----------------------------

# 3. Doubly Linked List

# -----------------------------

class DNode:
def **init**(self, data):
self.data = data
self.prev = None
self.next = None

class DoublyLinkedList:
def **init**(self):
self.head = None

```
def insert_end(self, x):
    new = DNode(x)
    if not self.head:
        self.head = new
        return

    temp = self.head
    while temp.next:
        temp = temp.next

    temp.next = new
    new.prev = temp

def insert_after(self, target, x):
    temp = self.head

    while temp:
        if temp.data == target:
            new = DNode(x)

            new.next = temp.next
            new.prev = temp

            if temp.next:
                temp.next.prev = new

            temp.next = new
            return
        temp = temp.next

    print("Target not found")

def delete_pos(self, pos):
    temp = self.head

    for _ in range(pos):
        if not temp:
            print("Position out of range")
            return
        temp = temp.next

    if not temp:
        print("Position out of range")
        return

    if temp.prev:
        temp.prev.next = temp.next
    else:
        self.head = temp.next

    if temp.next:
        temp.next.prev = temp.prev

def traverse(self):
    temp = self.head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")
```

# -----------------------------

# 4. Stack using SLL

# -----------------------------

class Stack:
def **init**(self):
self.head = None

```
def push(self, x):
    new = Node(x)
    new.next = self.head
    self.head = new

def pop(self):
    if not self.head:
        print("Stack Underflow")
        return None
    val = self.head.data
    self.head = self.head.next
    return val

def peek(self):
    if not self.head:
        return None
    return self.head.data
```

# -----------------------------

# 5. Queue using SLL

# -----------------------------

class Queue:
def **init**(self):
self.head = None
self.tail = None

```
def enqueue(self, x):
    new = Node(x)
    if not self.tail:
        self.head = self.tail = new
        return
    self.tail.next = new
    self.tail = new

def dequeue(self):
    if not self.head:
        print("Queue Underflow")
        return None
    val = self.head.data
    self.head = self.head.next
    if not self.head:
        self.tail = None
    return val

def front(self):
    if not self.head:
        return None
    return self.head.data
```

# -----------------------------

# 6. Balanced Parentheses Checker

# -----------------------------

def is_balanced(expr):
stack = Stack()
pairs = {')': '(', '}': '{', ']': '['}

```
for ch in expr:
    if ch in "({[":
        stack.push(ch)
    elif ch in ")}]":
        if stack.pop() != pairs[ch]:
            return False

return stack.head is None
```

# -----------------------------

# MAIN (Test Cases)

# -----------------------------

if **name** == "**main**":

```
print("\n--- Dynamic Array Test ---")
arr = DynamicArray()
for i in range(10):
    arr.append(i)
    arr.display()

print("Pop:", arr.pop())
print("Pop:", arr.pop())
print("Pop:", arr.pop())
arr.display()

print("\n--- Singly Linked List Test ---")
sll = SinglyLinkedList()
sll.insert_beginning(10)
sll.insert_beginning(5)
sll.insert_end(20)
sll.insert_end(30)
sll.traverse()

sll.delete(20)
sll.traverse()

print("\n--- Doubly Linked List Test ---")
dll = DoublyLinkedList()
dll.insert_end(1)
dll.insert_end(2)
dll.insert_end(3)
dll.insert_after(2, 99)
dll.traverse()

dll.delete_pos(1)
dll.traverse()

print("\n--- Stack Test ---")
st = Stack()
st.push(1)
st.push(2)
st.push(3)
print("Pop:", st.pop())
print("Peek:", st.peek())

print("\n--- Queue Test ---")
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Dequeue:", q.dequeue())
print("Front:", q.front())

print("\n--- Parentheses Checker ---")
tests = ["([])", "([)]", "(((", ""]
for t in tests:
    print(t, "->", "Balanced" if is_balanced(t) else "Not Balanced")
```
