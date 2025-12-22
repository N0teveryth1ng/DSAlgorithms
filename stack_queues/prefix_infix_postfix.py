# here we I will learn and solve problems about prefix , post fix, and infix. 

# postfix is basically about send up all the operands into stack and operators in a different string var
# and then output them based on their precedence or priority

def infix_to_postfix(s):

    stack = []
    ans = []
    
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3
    }
    
    for i in s:
        if i.isalnum():
           ans.append(i)

        elif i == '(':
            stack.append(i)
            
        elif i == ')':
            while stack and stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        
        else:
            while (stack and stack[-1] != '(' and
                   precedence[stack[-1]] >= precedence[i]):
                ans.append(stack.pop())
            stack.append(i)
            
            
    while stack:
        ans.append(stack.pop())
        
    return ''.join(ans)
    
    
# print(infix_to_postfix("a+b*c")) 
                 
             
             
             

def prefix_to_infix(s):
    stack = []
    
    for i in range(len(s) - 1, -1, -1):
        
        i = s[i]
        
        if i.isalnum():
            stack.append(i)
        else:
           
           operand1 = stack.pop()
           operand2 = stack.pop()
           
           expr = f"({operand1}{i}{operand2})"
           
           stack.append(expr)
           
    return stack

# print(prefix_to_infix("*+abc"))



# prefix to postfix 
def prefix_to_postfix(s):
    
    stack = []
    
    for i in range(len(s)-1, -1, -1):
        
        ch = s[i]
        
        if ch.isalnum():
            stack.append(ch)
        else:
            
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            expr = operand1 + operand2 + ch
            stack.append(expr)
            
    return stack[0]

# print(prefix_to_postfix("*+abc"))
       
       
       
# postfix to prefix 
def postfix_to_prefix(s):
    
    stack = []
    
    for ch in s:
        
        if ch.isalnum():
            stack.append(ch)
        else:
            
            oprnd1 = stack.pop()
            oprnd2 = stack.pop()
            
            expr = ch + oprnd1 + oprnd2
            stack.append(expr)
            
    return stack[0]
    
# print(postfix_to_prefix("ab+c*"))



# postfix to infix 
def postfix_to_infix(s):
    
    stack = []
    
    for i in s:
        
        if i.isalnum():
            stack.append(i)
        else:
            
            operand1 = stack.pop()
            operand2 = stack.pop()
            
            expr = operand1 + i + operand2
            stack.append(expr)
            
    return stack[0]

# print(postfix_to_infix("AB*C+"))



# infix to prefix 
def infix_to_prefix(s):
    
    stack = []
    output = []
    
    precedence = {
        '+' : 1,
        '-' : 1,
        '*' : 2, 
        '/' : 2, 
        '^' : 3
    }
    
    
    for i in range(len(s)-1, -1, -1):
    
        i = s[i]

        if i.isalnum():
            output.append(i)
            
        elif i == '(':
            stack.append(i)
            
        elif i == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
            
        else:
            while (stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[i]):  
                output.append(stack.pop())
            stack.append()
            
    while stack:
        output.append(stack.pop())
        
        
    return reversed(''.join(output))



print(infix_to_prefix("a+b*c"))
            
    
