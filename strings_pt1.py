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
            


