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
        
            
        


# test cases - - - [stack with size 6]
val = Queue(6)
val.enqueue(5)
val.enqueue(8)
val.enqueue(9)
val.enqueue(2)


print(val.arr) 
print(val.size)

