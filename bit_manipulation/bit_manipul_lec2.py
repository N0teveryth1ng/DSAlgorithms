# bit manipulation LEC-2 followed by the previous chapters



# count num of bit needed to flip convert from A to B

# rough implementation - - 
     
    #  3 = 011 
    #  4 = 100  
    # it counts as 3 bits to be changed 

# we can use XOR here
def flip(start, goal):
    
    res = 0
    while start or goal:
        if (start % 2) != (goal % 2):
            res += 1
            
        start = start >> 1
        goal = goal >> 1
        
    return res

# print(flip(7,4))
    
# 2nd approach - - - - - 
def flip2(start, goal):
    
    res = 0
    while start or goal:
        if (start & 1) != (goal & 1):
            res += 1
            
        start = start // 2
        goal = goal // 2
        
    return res

# print(flip2(7,4))
    
# 3rd approch - - -  - 
def flip3(start, goal):
    
    res = 0
    n = start ^ goal
    while n:
        res += n & 1
        n = n >> 1
        
    return res

# print(flip3(7,4)) 


# 4th approach - - brian kernighan method
def flip4(start, goal):
    
    res = 0
    n = start ^ goal
    while n > 0:
            n &= (n-1)
            res += 1
                
    return res
# print(flip4(7,4))



# single number
def single_nums(nums):
    
    res = 0
    for i in nums:
        res ^= i
    return res

# print(single_nums([4,6,4]))




# XOR of nums in given range
def xor_range(n):
    
    ans = 0
    for i in range(n+1):
        ans = ans ^ i
    return ans

# print(xor_range(5))

# - - - - optimla version xor range
def compact_xor(n):
    
    if n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n+1
    elif n % 4 == 3:
        return 0
    else:
        return n
    
# print(compact_xor(3))
        
#  - - - reverse the LEFT and RIGHT xor 
def righting(L, R):
    
    if L > R:
        L, R = R, L 
    return compact_xor(L-1) ^ compact_xor(R)    

# print(righting(3, 9))
        
        

# find the two nums appearing odd num of times 
def odd_nums():
    
    nums = [2,4,2,6,3,7,7,3]
    
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    
    res = []
    for j in freq:
        if freq[j] % 2 != 0:
            res.append(j)
            
    return res
    
# print(odd_nums())

# optimal approach of xor method 
def xor_method():
    
    nums = [2,4,2,6,3,7,7,3]
    
    ans = 0
    for i in nums:
        ans = ans ^ i
        
        diff = (ans) & (-ans)
        
        buck1 = 0
        buck2 = 0
        
        for j in nums:
            if j & diff:
                buck1 ^= j
            else:
                buck2 ^= j
                
                
    return buck1, buck2

# print(xor_method())



