# ṣtrings for part - 1 [ basic and easy strings problem ]

# valid parethesis - -  - -  using LIFO method
def valid_par():
    
    s = "()[]{}"
    
    stack = []
    pairs = { ')': '(', ']': '[', '}': '{' }
    
    for i in s:
            
        if i in pairs:
            if stack and stack[-1] == pairs[i]:  # if last elemnt mathed with opening to closing its gets removed
                stack.pop()  
            else:
                return False 
        else:
            stack.append(i)     # every opening elems gets added to the stack
            
            
    return True if not stack else False
                
                
# print(valid_par())


# remove the outermost paretheses
def remove_parentheses():
    
    s = "(()())(())"
    count = 0
    res = []
    
    for i in s:
        if i == "(":
            if count > 0:
                res.append(i)
            count += 1
        else:
            count -= 1
            if count > 0:
                res.append(i)
                
    return "".join(res)

# print(remove_parentheses())


            
# reverse a string
def reverse():
    
    s = "the sky is blue"
    
    s.strip()
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# print(reverse())



# largest odd nums - -  return the prefix of longest odd strings
def largest_odd():
    
    num = "52"
    for i in range(len(num) - 1, -1, -1):
        
        if int(num[i]) % 2 == 1:
            return num[:i+1]
        
    return ""
      
# print(largest_odd())    
    
  
  
# longest common prefix
def longest_prefix():
    
    strs = ["flower","flow","flight"]
    res = ""
    
    for i in range(len(strs[0])):
      for s in strs:
        if i >= len(strs) or s[i] != strs[0][i]:
            return res 
      res += strs[0][i]   
    return res

# print(longest_prefix())


# isomorpic alog

def isomorphic():
    
    
