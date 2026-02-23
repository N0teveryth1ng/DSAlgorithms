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




# zig zag or spiral traversal
def lc_103(node):
    
    if not node:
        return []
    
    
    q = deque([node])
    res = []
    left_right = True
    
    while q:
        current = []
        
        for _ in range(len(q)):
            node = q.popleft()
            current.append(node.val)
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
        if not left_right:
            current.reverse()
            
        res.append(current)
        left_to_right = not left_to_right
        
    return res



from collections import defaultdict
# lc - 987
def vertical(node):
    
    if not node:
        return []
    
    level = defaultdict(list)
    q = deque([(node, 0, 0)])
    
    min_col = float("inf") 
    max_col = float("-inf")
    
    while q:
        node, row, col = q.popleft()
        
        if col < min_col:
            min_col = col
            
        if col > max_col:
            max_col = col
            
        level[col].append((node.val, row))
        
        if node.left:
            q.append((node.left, row + 1, col - 1))
            
        if node.right:
            q.append((node.right, row + 1, col + 1)) 
            
    
    # sorting it in order by order
    res = []
    for i in range(min_col, max_col + 1):
        items = level[i]
        items.sort(key=lambda x: (x[1], x[0]))
        items = [val for val, _ in items]
        
        res.append(items)
        return res
    
    
    
    
    
# top view traversal - binary tree
def top_view(node):
    
    if not node:
        return []
    
    q = deque([(node, 0)])
    res = {}
    
    min_col = 0
    max_col = 0
    
    while q:
        node, col = q.popleft()
        
        min_col = min(min_col, col)
        max_col = max(max_col, col)
            
        if col not in res:
            res[col] = node.val
        
        if node.left:
            q.append((node.left, col - 1))
            
        if node.right:
            q.append((node.right, col + 1))
            
         
    return [res[col] for col in range(min_col, max_col + 1)]





# bottom view traversal - binary tree
def bottom_view(node):
    
    if not node:
        return []
    
    max_col = min_col = 0
    
    q = deque([(node, 0)])
    res = {}
    
    while q:
        node, col = q.popleft()
    
        min_col = min(min_col, col)    
        max_col = max(max_col, col)
        
        res[col] = node.val
            
        if node.left:
            q.append((node.left, col - 1))
            
        if node.right:
            q.append((node.right, col + 1))    
    
    
    return [res[col] for col in range(min_col, max_col + 1)]




# right view traversal - binary tree
def right_view(root):
    
    res = []
    
    def dfs(node, level):
        if not node:
            return []
        
        if level == len(res):
            res.append(node.val)
            
        dfs(node.right, level + 1)
        dfs(node.left, level + 1)
        
    dfs(root, 0)
    return res
    



# left view traversal - binary trees 
def left_view(root):
    
    res = []

    def dfs(node, level):
        
        if not node:
            return 
        
        if level == len(res):
            res.append(node.val)
            
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
        
    dfs(root, 0)
    return res






# boundary traversal - binary trees
def boundary(root):
    
    if not root:
        return []
        
    res = [root.val]
    
    # traverse left boundary
    def left_bound(node):
        if not node or (not node.left and not node.right):
            return
        res.append(node.val)
        if node.left:
            left_bound(node.left)
        else:
            left_bound(node.right)
            
    # traverse leaves
    def leaves(node):
        if not node or (not node.left and not node.right):
            return
        res.append(node.val)
        leaves(node.right)
        leaves(node.left)
        
        
    # traverse right boundary 
    def right_bondary(node):
        if not node or (not node.left and not node.right):
            return
        
        if node.right:
            right_bondary(node.right)
        else:
            right_bondary(node.left)
        res.append(node.val)
            
            
            
    if root.left:
       left_bound(root.left)

    leaves(root.left)
    leaves(root.right)
    
    if root.right:
        right_bondary(root.right)
        
        
    return res


        
    
    
    

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
""" HERE WE WILL SOLVE THE HARD PARTS OF BINARY TREES """

# print root to leaf path in binary tree
def root_leaf(node):
    
    if not node:
        return
    
    path = res = []
    
    path.append(node.val)
    
    if not node.left and not node.right:
        res.append(path.copy())
    else:
        root_leaf(node.left, path, res)
        root_leaf(node.right, path, res)
    
    path.pop()
    
    
    
    
# lc - 236
def LCA(node, p,q):
    
    if not node or node == p or node == q:
        return node
    
    left = LCA(node.left, p, q)
    right = LCA(node.right, p, q)
    
    if left and right:
        return node
   
    return left and right


 