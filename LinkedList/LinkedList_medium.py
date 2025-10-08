# Linked lists medium 


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
        
        
    # middle of a linked list    
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
        
        
    # detect a loop - optimal way 
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
    
             
        
    # linked list cycle - - - - find the starting point of a loop  
    def ll_cycle(self):
        
        if not self.head:
            return
        
        slow, fast = self.head, self.head
        
        # check if the loop exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next  
            
            if slow == fast:
                break
            else:
                return None
            
        # find the start of the cycle 
        fast = self.head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        
        return slow
    
        
        
        
        
    # length of the loop - - - - brute force method [ using map ]
    def  len_loop_brute(self):
        
        if not self.head:
            return 0 
        
        store = set()
        
        temp = self.head
        while temp:
            if temp in store:
                
                loop_found = temp
                count = 1
                temp = temp.next
                
                while temp != loop_found:
                    count += 1
                    temp = temp.next  
                    
                return count 
            
            store.add(temp)
            temp = temp.next  
        
        
        
    # length of loop - - - optimal method [ using slow, fast ] 
    def len_loop_optimal(self):
            
        if not self.head:
            return 
        
        slow, fast = self.head, self.head
        
        while fast and fast.next:
            slow = slow.next  
            fast = fast.next.next  
            
            if slow == fast:
                
                count = 1
                temp = slow.next       
                while temp != slow:
                   count += 1
                   temp = temp.next  
                   
                return count
                  
        return 0
    
    
    # check if a LL is palindrome or not
    def palindrome_ll(self):
        
        if not self.head:
            return
        
        stack = []
        
        temp = self.head
        while temp:
            stack.append(temp.val)
            temp = temp.next
            
        temp = self.head
        while temp:
            if temp.val != stack.pop():
                return False
            temp = temp.next
            
        return True
    
    
    
    def palindome_optimal(self):
        
        if not self.head:
            return
        
        # check for mid 
        slow, fast = self.head, self.head
        temp = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
            
        # reverse the 2nd half
        prev = None
        while slow:
           temp = slow.next
           slow.next = prev
           prev = slow
           slow = temp
           
        # compare both  
        left, right = self.head, prev
        while right:
            if left.val != right.val:
                return False
            
            left = left.next
            right = right.next
            
        return True   
        
            
    
    # odd and even linked list
    def odd_even_ll(self):
        
        if not self.head:
            return
        
        stack = []
        
        temp = self.head
        while temp:
            
            # store the odds one in stack
            if temp % 2 != 0:
                stack.append(temp)
                
            temp = temp.next
            
        return temp + stack
    
                
        
    # display the LL in terminal 
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.val, end=" - ")
            temp = temp.next
        print("None") 
    
    
ll = Dlinkedlist()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(9)
ll.append(1)
ll.display_forward()

# print('mid elem - ', ll.mid_of_ll())
# print('slow, fast - ', ll.tortoise())

# print('after reverse - ')
# ll.rev_ll()
# ll.rev_ll_optimal()

# print('detect a loop - ', ll.detect_loop())

# print('start of cycle - - ', ll.ll_cycle().val)   

print('palindrome check - ', ll.palindrome_ll())
ll.display_forward() 

        
        
        
        