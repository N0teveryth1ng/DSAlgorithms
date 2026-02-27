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