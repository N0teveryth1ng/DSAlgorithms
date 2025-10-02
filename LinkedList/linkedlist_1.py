# Covering the basics of link lists and all 

"""  
Linked List - - 
 
 A simple structure where each node contains the data and next pointer (link)for the next node  in seqence 
"""

# Singly Linked List - - - - - One way directed 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None
        
        
        
    # insert at data in LL
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
      
    # search for target
    def search(self, val):
        temp = self.head
        while temp:
            if temp.data == val:
               return True
            temp = temp.next
        return False
    
    
    
    
    #  - - - - - - delete elems - -  - - -- -
    
    # remove heads
    def removeHead(self, val):
        if self.head is None:
            return None
        
        # value is in head check
        if self.head.data == val:
            self.head = self.head.next
            return
        
        # check next vals
        temp = self.head
        while temp.next:
            if temp.next.data == val:
                 temp.next = temp.next.next 
                 return
            temp = temp.next 
        
        
        
        
    # remove tail only  - - -  
    def removetail(self):
        if self.head is None:
            return None
        
        if self.head.next == None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next 
            
        temp.next = None        
        
        
        
    # remove the kth element
    # gien - [ 1, 3, 5]
    def kth_elem(self, k):
        if not self.head:
            return None
        
        # if head is Kth elem
        if k == 1:
            self.head = self.head.next
            return
        
        # for mid - tail  
        temp = self.head
        count = 1
        while temp and count < k - 1:
            temp = temp.next
            count += 1
            
        if temp and temp.next:
            temp.next = temp.next.next 
        
        
        
    # remove the element by value
    def remove_element(self, elem):
        if not self.head:
            return 
        
        if elem == 1:
            self.head == self.head.next
            return
        
        temp = self.head
        count = 1
        while temp and count < elem - 1:
            temp = temp.next
            count += 1
            
        if temp and temp.next:
            temp.next = temp.next.next 
            
            
            
    #  - - -  - - - - - - insert elems  - - - -  - - - -- - 
            
    # insert head only - - -  
    def insert_head(self,data):
        
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node   
        
         
     
    # insert tail only  - - - 
    def insert_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next    
        
        new_node.next = temp.next
        temp.next = new_node
            
            
            
            
    #  insert in Kth element 
    def kth_insert(self, data, k):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
         
        if k == 1:
            new_node.next = self.head
            self.head = new_node
            return 
        
        temp = self.head
        count = 1
        while temp and count < k - 1:
            temp = temp.next
            count += 1
            
        if not temp:
            return
        
        new_node.next = temp.next
        temp.next = new_node
        
        
        
    #   insert by position 
    def insert_pos(self, data, pos):
        
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        
        temp = self.head
        count = 1
        while temp and count < pos - 1:
            temp = temp.next
            count += 1
            
        if not temp:
            return
        
        new_node.next = temp.next
        temp.next = new_node
        
            
    
    # display the appended 
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print('None')
        
        
        
#  - - - -   running singly LL  - - - - - -
        
#  running tests 
ll = linked_list()
# ll.append(1)
# ll.append(3)
# ll.append(5)

# ll.display()

# # print(ll.removetail()) # - - - - calling remove tail 

# print('after removing - ') # - - - - after removing the tail 
# ll.kth_elem(2)
# ll.insert_tail(9)
# ll.kth_insert(8)
# ll.display()

    

    
    
    






#  - - - - - - -  - - DOUBLY LINKED LIST - - - - - - - - - - - - -


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
        
        
    
    
    def insert_elem(self, val):
        
        new_node = dNode(val)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        
        
        
        
        # DLL head insert 
    def insert_head(self, val):
        new_node = dNode(val)
        self.head.next = self.head
        self.head = new_node
        
        
        
        # tail insert DLL
    def insert_tail(self, val):
        new_node =  dNode(val)
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next 
        temp.next = new_node  # - for inserting elem at next node 
        temp.prev = new_node  # - for inserting elem at prev node

        
        # Kth insert for DLL
    def insert_kth(self, val, k):
        new_node = dNode(val)
        if not self.head:
            self.head = new_node
            return
        
        if k == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        
        temp = self.head
        count = 1
        while temp.next:
            temp = temp.next
            count += 1
            
        if not temp:
            return
        
        new_node.next = temp.next
        temp.next = new_node
        
        
        
    # delete for elemt 
    def delete_head(self):
        if not self.head:
            return
        
        if self.head.data == None:
            self.head = None  
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None
        
        
    # 
    def         
            
        
        
    
            
        
        
        
    
        
        