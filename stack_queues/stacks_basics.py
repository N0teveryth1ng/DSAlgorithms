# stacks basics (lecture 1 ) - - - - - initials 

# stack - implementing push and pop inside stack using arrs - LIFO
class Stack:
    def __init__(self, size):
        self.size = size
        self.arr = ["_"] * size
        self.top = -1
        
    # push values in stack
    def push(self, x):  
        if self.top == self.size - 1:
            raise Exception ("stack full")
            
        self.top += 1
        self.arr[self.top] = x
        
        # top pointer moves first and then elem gets added in stack


    # pop values from stack
    def pop(self):
        if self.top == -1:
            raise Exception("Stack empty")
        
        value = self.arr[self.top] 
        self.top -= 1
        return value
        
        
        
        
# queue - implementing queue using arrs  - - - [FIFO]
class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [0] * size
        self.front = 0
        self.rear = -1
        


    # push in queue - - - FIFO
    def enqueue(self, x):
        if self.rear == self.size - 1:
            raise Exception("Queue full")
        
        self.rear += 1
        self.arr[self.rear] = x
        
        
    def dequeue(self):
        if self.front > self.rear:
            raise Exception("qeueue empty")
        
        val = self.arr[self.front]
        self.front += 1
        return val
        
            





# built in deque
from collections import deque

# LC - 225  - - - implement stack using queue
class Mystack:
    def __init__(self):
        self.q = deque()
    
    def push(self, x):
        self.q.append(x)
        
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())
        
    def pop(self):
        return self.q.popleft()
    
    def top(self):
        return self.q[0]
    
    def empty(self):
        return len(self.q) == 0
         



#  - - - LC - 232 [implement queue using stack ]
class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push_stk(self, x):
        self.s1.append(x)
        
    def pop_stk(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    
    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]
    
    def empty(self):
        return max(len(self.s1), len(self.s2)) == 0
    
    
    
      





# test cases - - - [stack with size 6]
# val = Queue(6)
# val.enqueue(5)
# val.enqueue(8)
# val.enqueue(9)
# val.enqueue(2)


# print(val.arr) 
# print(val.size)





# implementing stack using LL - FIFO
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Stack_LL:
    def __init__(self):
        self.head = None
    
    def push_ll(self, x):
        node = Node(x)
        node.next = self.head
        self.head = node
        
    def pop(self):
        if not self.head:
            raise Exception("nothing to remove")
        val = self.head.val
        self.head = self.head.next
        return val
        
    def peek(self):
        if not self.head:
            raise Exception('nothing to peek')
        return self.head.val
        
    def empty(self):
        return self.head is None
    
    

# implement queue using LL - FIFO
class Queue_LL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.head = None
        
    def push_enque(self, x):
        new = Node(x)
        if not self.front:
           self.front = new
           self.rear = new
        else:
           self.rear.next = new
           self.rear = new
        
        
    def pop_deque(self):
        if not self.front:
            raise Exception("LL cleared")
          
        data = self.front.val
        self.front = self.front.next
        
        if not self.front:
            self.rear = None
            
        return data




def valid_par(s):
    stack = []
    pairs = { ')': '(', ']': '[', '}': '{' }
    
    for i in s:
        if i in pairs:
            if stack and stack[-1] == pairs[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
            
    return not stack

        
# print(valid_par("(()"))
    
        
def push(self, x):
    
    self.s1.append(x)
    if not self.s2 and x <= self.s2:
        s2.append(x) 