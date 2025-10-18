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
        
        
    
    # delete the occurences in a DLL 
    def delete_occurence(self, key):
        
        if not self.head:
            return
        
        temp = self.head
        
        while temp:
            next_node = temp.next 
            
            # if head is val then delete
            if temp.val == key:
                # if the node to delete is head 
                if temp == self.head:
                   self.head = temp.next  
                   if self.head: 
                      self.head.prev = None
            else:
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
    
    
    # optimal approach  - - -  pairs of sum - - ( very similar to binary search )   
    def optimal_pairs_sum(self, target_sum):
        
        if not self.head:
            return []
        
        temp = self.head
        left = temp
        
        right = self.head
        while right.next:
            right = right.next 
        
        store = []
        
        while left != right and left.prev != right:
            
            current_sum = left.val + right.val
            
            if current_sum == target_sum:
                store.append((left.val, right.val))
                left = left.next
                right = right.prev
            elif target_sum < current_sum:
                right = right.prev  
            else:
                left = left.next
                
        return store        
    
    
    # remove the duplicates from a sorted DLL
    def remove_duplic(self):
        
        if not self.head:
            return
        
        temp = self.head
        while temp and temp.next:
            if temp.val == temp.next.val:
                next_node = temp.next.next  
                temp.next = next_node
                if next_node:
                    next_node.prev = temp
            else:
                temp = temp.next  
        
        return temp
    
    
    
    # 
    
    
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
ll.append(3)
ll.display_forward()


# print("pairs of sum - ", ll.pairs_sum(6))      
# print("optimal pairs sum - ", ll.optimal_pairs_sum(8))
print(" remove duplicates in dll - ", ll.remove_duplic())
         
ll.display_forward()
        
        
        
        
        
        
    
                
                 
        
            