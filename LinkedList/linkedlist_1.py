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
        if self.head == None:
            return None
        
        if self.head.next == None:
            self.head = None
            return
        
        temp = self.head
        while temp.next.next:
            temp = temp.next 
            
        temp.next = None        
        
    # display the appended 
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print('None')
        
ll = linked_list()
ll.append(1)
ll.append(3)
ll.append(5)

print('before removing tail')
ll.display()

print(ll.removetail()) # - - - - calling remove tail 

print('after removing tail - ') # - - - - after removing the tail 
ll.display()
    
        
        
        
    