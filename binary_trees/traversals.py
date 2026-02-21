# Taversals   
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.val)


# tree nodes
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



# check for balanced binary tree - [lc 110]
def balanced_binary(node):
    
    if not node:
        return [True, 0]
    
    left, right = balanced_binary(node.left), balanced_binary(node.right)
    balanced = (left[0] and right[0] and 
                abs(left[1] - right[1]) <= 1)    
    
    return [balanced, 1 + max(left[1], right[1])]

# print(balanced_binary(C))




# diameter binary tree 
def diameter(node):
    
    diaMet = 0
    
    def height(n):
        nonlocal diaMet
        if not n:
            return 0
        
        left_height = height(n.left)
        right_height = height(n.right)
        diaMet = max(diaMet, left_height + right_height)    
        return 1 + max(left_height, right_height)
    
    height(node)
    return diaMet

# print(diameter(A))



# binary tree maximum path sum [lc - 124]
def max_sum(node):
    max_path = float('-inf')
    
    def dfs(n):
        nonlocal max_path
        if not n:
            return 0
        
        left = max(dfs(n.left), 0)
        right = max(dfs(n.right), 0)
        
        # Path through this node
        max_path = max(max_path, n.val + left + right)
        
        # Return best one-sided path
        return n.val + max(left, right)
    
    dfs(node)
    return max_path

# print(max_sum([-10,9,20,0,0,15,7]))
    
    
    
    
    
# same tree - [lc - 100] 
def same_tree(p, q):
    
    if not p and not q:
        return True
    
    if not p or not q:
        return False
    
    if p.val != q.val:
        return False
    
    return same_tree(p.left, q.left) and same_tree(p.right, p.right)





    