# I will continue to solve problems of monotnic stacks and queues

# LC - 496 
def next_gret():

    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]
    
    stack = []
    
    for num in n1:
        found = -1
        
        for i in range(len(n2)):
            if n2[i] == num:
                
                for j in range(i+1, len(n2)):
                    if n2[j] > i:
                        found = n2[j]
                        break    
                break
            
        stack.append(found)
    return stack
    

# print(next_gret())


# next great element
def next_great_elem(num1, num2):
    
    stack = []
    mappo = {}
    
    for i in reversed(num2):
        while stack and stack[-1] <= i:
            stack.pop()
            
        if stack:
            mappo[i] = stack[-1]
        else:
            mappo[i] = -1
            
        stack.append(i)
        
    return [mappo[n] for n in num1]
    
# print(next_great_elem([4,1], [1,2,3,4]))



# next big element - II 
def next_big_elem_2(s):
 
    n = len(s)
    res = [-1] * n
    
    for i in range(n):
        found = -1
        for j in range(1, n):
            next_idx = (i + j) % n
            if s[next_idx] > s[i]:
                found = s[next_idx]
                break
            
        res[i] = found
    
    return res

# print(next_big_elem_2([1, 2, 1]))        
        
            
# next big elem II - optimal solution [VVP]
def next_big_elem_optimal(s):
    
    n = len(s)
    res = [-1] * n
    stack = []
    
    for i in range(2 * n):
        idx = i%n
        while stack and s[idx] > s[stack[-1]]:
           popped = stack.pop()
           res[popped] = s[idx]
           
        if i < n:
            stack.append(i)
            
    return res 

# print(next_big_elem_optimal([1, 2, 1]))



# next smaller element  - - brute force [1]
def small_elem(s):
    
    stack = []
    mappo = {}
    
    for i in range(len(s)-1, -1, -1):
        while stack and stack[-1] >= s[i]:
            stack.pop()
            
        if stack:
            mappo[i] = stack[-1]
        else:
            mappo[i] = -1
              
        stack.append(i)
        
    return mappo 
    
# print(small_elem([1,2,3,4]))


# next small element -- brute force approach [2]
def small_elems(s):
    
    n = len(s)
    stack = [-1] * n
    
    for i in range(n):
        for j in range(i+1, n):
            if s[i] > s[j]:
                stack[i] = s[j]
                break 
            
    return stack
        
# print(small_elems([1,2,3,4]))



# next small element -- optimal approach 
def small_element(s):

    n = len(s)    
    res = [-1] * n
    stack = []
    
    for i in range(2 * n):
        idx = i % n
        while stack and s[idx] < s[stack[-1]]:
            popped = stack.pop()
            res[popped] = s[idx]
            
        
        if i < n:
            stack.append(idx)
            
    return res

# print(small_element([1,6,3,9]))
        
        