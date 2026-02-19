# Taversals 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)

# 
A = TreeNode(1)
B =  TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)


A.left = B
A.right = C
B.left = D
B.right = E
C.right = F


# print(A)

# lc 144 - preorder traversal
def preorder(node):
    
    if not node:
        return
    
    print(node)
    preorder(node.left)
    preorder(node.right)
    
# print(preorder(A))
    
    
#  in order traversal
def inorder(node):
    
    if not node:
        return 
    
    inorder(node.left)
    print(node)
    inorder(node.right)
    
# print(inorder(A))
    
    
# post order traversal
def postorder(node):
    
    if not node:
        return
    
    postorder(node.left)
    postorder(node.right)
    print(node)
    
# print(postorder(A))



from collections import deque

# level order travesal
def level_order(node):
    
    q = deque()
    q.append(node)
    
    while q:
        node = q.popleft()
        print(node)
        
        if node.left:
            q.append(node.left)
        
        if node.right:
            q.append(node.right)
            
# print(level_order(A))
        

# level order based on (leetcode format)
def test(root):
    
    if not root:
        return []
    
    res = []
    
    q = deque()
    q.append(root)
    
    while q:
        current = []
        for _ in range(len(q)):
            node = q.popleft()
            current.append(node.val)
            
            if  node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        res.append(current)
            
    return res
                



# maximum depth in BT 
def max_depth_BT(node):
    
    if not node:
        return 0
    
    left = max_depth_BT(node.left)
    right = max_depth_BT(node.right)
    return 1 + max(left, right)

# print(max_depth_BT(A))



# check for balanced binary tree
def balanced_binary(node):
    
    if not node:
        return False
    
    while node.left < node.right:
        left = balanced_binary(node.left)
        right = balanced_binary(node.right) 
        abs(height(left) - height(right)) <= 1 
        
        