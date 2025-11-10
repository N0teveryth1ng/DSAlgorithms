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
        
        
        
# N - Queens [LC - 51]
def n_queens(n):
    
    rows, cols = len(n), len(n[0])
    
    def dfs(r,c,i):
        
        if i == len(n):
            return True
        
        if r > 0 or  c > 0 or r > len(rows) or c > len(cols):
            return False
        
        found = ( dfs(r + 1, c, i+1) or
                  dfs(r - 1, c, i+1) or
                  dfs(r, c + 1, i+1) or
                  dfs(r, c - 1, i+1))
        
        return found
    
    for r in range(rows):
        for c in range(cols):
            if [r][c] == n[0]:
                return True
            
    return False

    
    
 
         
    
