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
                    

                    
                
        
        