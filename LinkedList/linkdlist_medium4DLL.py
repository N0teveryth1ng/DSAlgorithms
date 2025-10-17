# I will be continuing with medium probelms if DLL 

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
        
        
    
    # delete the occurences in a LL 
    def delete_occurence(self, key):
        
        if not self.head:
            return
        
        while temp:
            next_node = self.head.next 
            
            # if head is val then delete
            if self.head.val == key:
                if temp == self.head:
                   self.head = self.head.next  
                   if self.head: 
                      next_node = self.head
                      self.head.prev = None
            else:
                temp = self.head
                # connect it with the prevs nodes after skipping
                if temp.prev:
                   temp.prev.next = temp.next
                if temp.next:
                    temp.next.prev = temp.prev  
                

        temp = next_node
        
        
        
    # find pairs with given sum in DLL - - - ( brute force method )
    def pairs_sum(self, target_sum):
        
        if not self.head:
            return
           
        temp1 = self.head
        store = []
        
        while temp1:
            temp2 = temp1.next
            while temp2:
                if temp1.val + temp2.val == target_sum:
                   store.append((temp1.val, temp2.val))
                temp2 = temp2.next  
            temp1 = temp1.next 
            
        return store
    
    
    # optimal approach 
    def optimal_pairs_sum(self, target_sum):
        
        if not self.head:
            return []
        
        left = self.head
        store = []
        
        while left:
            right = left.next
            if left.val + right.val == target_sum:
                store.append(left.val, right.val)
            if left.val + right.val < target_sum:
                right = right.prev
            else:
                left = left.next
                
        return store        
    
    
    
    
    # display the LL in terminal 
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.val, end=" - ")
            temp = temp.next
        print("None") 
    
    
    
    
    
ll = Dlinkedlist()
ll.append(5)
ll.append(6)
ll.append(9)
ll.append(3)
ll.display_forward()


# print("pairs of sum - ", ll.pairs_sum(6))      
         
ll.display_forward()
        
        
        
        
        
        
    
                
                 
        
            