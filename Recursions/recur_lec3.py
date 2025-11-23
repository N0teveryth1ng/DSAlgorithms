""" lecture - 3 of recursions """


# palindrome partitioning  ----- [LC - 131]
def palindrome_part(s):
    
    res = []

    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def dfs(i, current):
        if i == len(s):
            res.append(current.copy())
            return
        
        for end in range(i, len(s)):
            sub = s[i:end+1]
            
            if is_palindrome(sub):
                current.append(sub)
                dfs(end + 1, current)
                current.pop()
                    
    dfs(0, [])
    return res
        
        
# print(palindrome_part("aab"))
                    
                    
                    
# word search
def matrix_word(board, word):
    
    rows, cols = len(board), len(board[0])
    
    def dfs(r,c,i):
        if i == len(word):
            return True
        
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
        
        temp = board[r][c]
        board[r][c] = "#"
        
        found = ( dfs(r + 1, c, i+1) or
                   dfs(r - 1, c, i+1) or
                   dfs(r, c + 1, i+1) or
                   dfs(r, c - 1, i+1)) 

        board[r][c] = temp
        return found
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r,c,0):
                return True    
    
    return False

# test of the fucntion  
board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

# print(matrix_word(board, "ABCCED"))
        
        
        
# N - Queens [LC - 51] - - - -  [ didn't undetstood shit about this topic]
def n_queens(n):
    
    res = []
    board = [["."] * n for _ in range(n)]
    
    col = set()
    pos_diag = set()  # r + c
    neg_diag = set()  # r - c 

    def backTrack(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
            return
        
        for c in range(n):
            if c in col or  (r+c) in pos_diag or (r-c) in neg_diag:
                continue
            
            col.add(c)
            pos_diag.add(r+c)
            neg_diag.add(r-c)
            board[r][c] = "Q"
            
            backTrack(r + 1)
            
            col.remove(c)
            pos_diag.remove(r+c)
            neg_diag.remove(r-c)
            board[r][c] = "."
        
    backTrack(0)
    return res

# print(n_queens(4))
     

# rat in a maze - - - -  [ have to reach form (0,0) to (n-1) ]
def rat_maze(maze):
    
    n = len(maze)
    res = []
    path = []
    
    visited = [[False] * n for _ in range(n)]
    
    def dfs(r,c):
        
        # destination reached
        if r == n-1 and c == n-1:
            res.append("".join(path))
            return
        
        # mark it visited
        visited[r][c] = True
        
        # DLRU - dowm, left, right, up
        directions = [
            (1,0,"D"),
            (0,1,"R"),
            (0,-1,"L"),
            (-1,0,"U")
        ]
        
        
        # direction rows and drection cols
        for dr, dc, move in directions:
            nr = r + dr  # new rows 
            nc = c + dc  # new cols
            
            if 0 <= nr < 0 and 0 <= nc < n and maze[nc][nr] == 1 and not visited[nr][nc]:
                path.append(move)
                dfs(r,c)
                path.pop()
                
        # backtrack it 
        visited[r][c] = False
        
    
    if maze[0][0] == 1:
        dfs(0,0)
        
    return res  
        


# word break --------------- [ DIDNT UNDERSTOOD SHIT ABOUT THIS  ]
def word_break(s, wordBreak):
    
    dp = [False] * (len(s) + 1)  
    dp[len(s)] = True
    
    for i in range(len(s) - 1, -1, -1):
        for j in wordBreak:
            if (i + len(j)) <= len(s) and s[i : i + len(j)] == j:
                if dp[i + len(j)]:
                   dp[i] = True
                   break
            
    return dp[0]
            
            
# M coloring problem
def m_coloring():
    
    # check for safe move
    def is_safe(graph, color, node, col):
        for neighbour in graph[node]:
            if col[neighbour] == color:
                return False
        return True
    
    # run recursion
    def recursion(node, graph, m, col):
        
        if node == len(graph):
            return True
        
        for i in range(1, m+1):
            if is_safe(graph, node, col, m):
                col[node] = i
                
                if recursion(node + 1, graph, m, col):
                    return True          
                col[node] = 0
                
        return False
                
                
    # graph_coloring
    def graph_color(graph, m):
        
        col = [0] * len(graph)
        return recursion(0, graph, m, col)            
        
    
    
# sudoko solver - - - -  [ LC - 37 ]
def is_valid(board, rows, cols, c):
    
    for i in range(1, 9):
        if board[rows][i] == c:
            return False
        
        if board[i][cols] == c:
            return False
        
    # 3x3 box cehck
    box_r = (rows // 3) * 3
    box_c = (cols // 3) * 3
    
    for i in range(box_r, box_r + 3):
        for j in range(box_c, box_c + 3):
            if board[i][j] == c:
              return False
          
    return True
    

def soduko_solver(board):
    
    for i in range(9):
        for j in range(9):
            
            if board[i][j] == ".":  
              for c in "123456789":            
                if is_valid(board, i, j, c):
                    board[i][j] = c
                   
                    if soduko_solver(board):
                        return True
                    
                    board[i][j] = "."
                    
              return False
            
    return True
         

# print(soduko_solver(board))


# expression and operators - - - - - - - [ LC - 282 ]
def expression_opt(num, target):
    
    res = []
    n = len(num) 
        
    def solve(index, path, calcVal, lastNum):
        
        if index == n:
            if calcVal == target:
               res.append(path)
            return
        
        
        """  NOT DONE DUE TO LACK OF UNDERSTANDING  """   
            
           
            

