# Linked lists medium 

# middle of a linked list

class dNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None    
        
class Dlinkedlist:
    def __init__(self):
        self.head = None
        
        
    def append(self, val):
        new_node = dNode(val)
        
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp
        
        
    # find the mid of the LL 
    def mid_of_ll(self):
        
        if not self.head:
            return
        
        temp = self.head
        count = 0
        
        while temp:
            temp = temp.next
            count += 1
            
        mid_node = (count // 2) 
        
        temp = self.head
        for _ in range(mid_node):
            temp = temp.next
        
        return temp.val
    
    # slow - fast pointer method  - - (most efficient one) - - tortoise and hare 
    def tortoise(self):
        if not self.head:
            return

        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        return slow.val
        
         
         
    # reverse a LL ( iterative ) 
    def rev_ll(self):
        
        if not self.head:
            return
        
        temp = self.head
        stack = []
        
        while temp:
            stack.append(temp.val)
            temp = temp.next
            
        new_head = stack.pop()    
        temp = new_head
        
        while stack:
            temp.next = stack.pop()
            temp = temp.next
            
        temp.next = None
        return new_head
    
    # iterative reversal 
    def rev_ll_optimal(self):
        
        if not self.head:
            return
        
        temp = self.head
        prev = None
        
        while temp:
            front = temp.next
            temp.next = prev
            prev = temp
            temp = front
            
        return prev
    
    
    
    # recursive reversal     - - - - - - still the worst way to deal 
    def rev_ll_recurse(self):
        head = self.head
        def recurse(head):    
            
            if self.head is None or self.head.next is None:
                return self.head
            
            new_head = recurse(head.next)
            
            self.head.next.next = self.head
            self.head = None
            
            return new_head
        
        
        
    # detect a loop - - - -  brute force method 
    def detect_loop(self):
        
        if not self.head:
            return
        
        store = set()
        
        temp = self.head
        while temp:
            if temp in store:
                return True
            store.add(temp)
            temp = temp.next
            
        return False
        
        
    # detetc a loop - optimal way 
    def detect_loop_optmal(self):
        
        if not self.head:
            return
        
        slow, fast = self.head, self.head
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next 
            
            if slow == fast:
                return True
        
        return False
 
        
    
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.val, end=" <-> ")
            temp = temp.next
        print("None") 
    
    
ll = Dlinkedlist()
ll.append(5)
ll.append(10)
ll.append(15)
ll.append(20)
ll.append(25)
ll.display_forward()

# print('mid elem - ', ll.mid_of_ll())
print('slow, fast - ', ll.tortoise())

print('after reverse - ')
# ll.rev_ll()
ll.rev_ll_optimal()

print('detect a loop - ', ll.detect_loop())
ll.display_forward() 
     
     

        
        
        
        