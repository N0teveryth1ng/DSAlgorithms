"""" WE WILL SOLVE PROBLEMS REALATED TO 
     --------  BINARY SEARCH TREE --------- 
"""




# intro to BST
""" BST is same as binary seach just in tree format. Where 

    [Left < root < Right] 
    
    if val == node.val:
       return found
    ellid val < node.val:
        go left
    else:
        go right
"""




# 


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
    
    
    
    # search in BST - [lc - 700]
    def searchBST(self, node, val):
        
        if not node:
            return
        
        if val == node.val:
            return node
        elif val < node.val:
            return self.searchBST(node.left, val)
        else:
            return self.searchBST(node.right, val)
            
        
        
        
    # min/max in BST
    def minimum(self, node):
        
        while node.left:
            node = node.left
        return node.val
    
    
    def maximum(self, node):
        while node.right:
            node = node.right
        return node.val
    
    
    
    
    # floor and ceil val in BST
    def floor_ceil(self, node, target, floor=None, ceil=None):
        
        if not node:
            return floor, ceil
        
        if node.val == target:
            return target
    
        if target < node.val:
            ceil = node.val
            floor, ceil = self.floor_ceil(node.left, target, floor, ceil)
        else:
            floor = node.val
            floor, ceil = self.floor_ceil(node.right, target, floor, ceil)
            
        return floor, ceil
            
        
            
            
    # insert a given node inside a BST
    def insert_node(self, node, val):
        
        if not node:
            return TreeNode(val)
        
        if val < node.val:
            node.left = self.insert_node(node.left, val)
        else:
            node.right = self.insert_node(node.right, val)
             
        return node
        
        
        
    # ḍelete a node from BST - 
    def deleet(self, root, key):
        
        if not root.left and not root.right:
            return None
        
        if key < root.val:
            self.deleet(root.left, key)
        elif key > root.val:
            self.deleet(root.right, key)
        else:
            
            # found node to delete
            if not root.right:
                 return root.left
            if not root.left:
                return root.right
            
            
            # two childrens
            succ = root.right
            while succ.left:
                succ = succ.left
            root.val = succ.val
            root.right = self.deleet(root.right, succ.val)
                
        return root
    
    
    
    
   
   # Kth largest/smallest element in BST - [lc - 230]
    def Kth_largest(self, node, k):
       
        if not node:
           return
       
        if k < node.val:
            self.Kth_largest(node.left, k)
        elif k > node.val:
            self.Kth_largest(node.right, k)
            
             
        