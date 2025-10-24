# I will be continuing with medium probelms if DLL 


class dNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None    
        self.random = None
        
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
    
    
    
    # reverse nodes in K-grp
    def reverse_LL_k(self):
        
        if not self.head:
            return
        
        dummy = dNode(0)
        group_prev = dummy
        dummy.next = self.head
        
        while True:
            kth = self.get_kth(group_prev, kth)
            if not kth:
                break
            
            grp_next = kth.next  
            
        
            # reversing 
            curr, prev = group_prev.next, grp_next
            while curr != grp_next:
                temp = curr.next  
                curr.next = prev
                prev = curr
                prev = temp
                
            
            # linking the nodes
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
        
        return dummy.next
    
        # carrier fucntion of find kth group
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next 
            k -= 1
        return curr
        
        
    
    # rotate a linkedlist by kth elem right
    """ 1 -> 2 -> 3
             |
             7 -> 8 -> 9 """
         
    def rotate_linkedlist(self, k):
        
        if not self.head:
            return 
        
        # find the tail
        tail = self.head
        count = 1
        while tail.next:
            tail = tail.next
            count += 1
        
        # check for Kth elem
        k = k % count
        if k % count == 0:
            return self.head
        
        # find the new tail and head
        new_tail = self.head
        for _ in range(count - k - 1):
            new_tail = new_tail.next
            
        new_head = new_tail.next
        new_tail.next = None
        tail.next = self.head
        self.head = new_head
        return self.head
    
    
    
    # flatenning of LL - ---  brute force method
    def flattening_LL(self):
        if not self.head:
            return
        
        arr = []
        temp = self.head
        
        while temp:
            
            # chck nodes side ways
            if temp.next:
                arr.append(temp.next)
                
            # check for child if: True then go deeper
            if temp.child:
                temp.next = temp.child
                temp.child = None
            elif arr:
                temp.next = arr.pop()
                
            temp = temp.next 
    
        return self.head
    
    
    # optimal way of flatenning a LL - - - -  - iterative approach
    # both optimal and brute force is almost same just its a bit of change in pointers
    def optimal_flatenning(self):
        
        if not self.head:
            return
        
        stack = []
        temp = self.head
        while temp:
            if temp.child:
                if temp.next:
                  stack.append(temp.val)
                temp.next = temp.child
                temp.child = None   
                
            if not temp.next and stack:
                stack.pop()
                
            temp = temp.next
            
        return self.head    
    

    # clone a LL with next and random pointers using hashing - - - [ better force ]
    # it can be optimised but i will get confused with the pointers  - - i'll try to learn it later
    def clone_rand(self):
        
        if not self.head:
            return
        
        # map all the copies of the values in a node
        old_new = {}
        
        temp = self.head
        while temp:
            old_new[temp] = dNode(temp.val)
            temp = temp.next
        
        # connect the cloned nodes with original links
        temp = self.head
        while temp:
            clone = old_new[temp]
            clone.next = old_new.get(temp.next)
            clone.random = old_new.get(temp.random)
            temp = temp.next 
            
        # set the head of new node 
        return old_new[self.head]
    
    
        

            
    
    
     
    
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
# print(" remove duplicates in dll - ", ll.remove_duplic())
# print("rotate ll from rifht by kth - ", ll.rotate_linkedlist(3))

print("clone of a LL points to next and random - ", ll.clone_rand())




ll.display_forward()
        
        
        
        
        
        
    
                
                 
        
            