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


