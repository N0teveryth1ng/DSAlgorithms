# We will be continuing with recursions and its problems in order to get a strong hold of it

# My ATOI
def my_atoi():
    
    s = " -42abc"
    
    sign = 1
    res = 0
    i = 0
    n = len(s)
    
    s = s.strip()
    
    if not s:
        return
    
    # chek for neg values
    if s[0] == '-' or s[0] == '+':
        if s[0] == '-':
            sign = -1
        i += 1
        
    # check for is digit or not
    while i < n and s[i].isdigit():
        res = res * 10 + int(s[i])
        i += 1
        
    res *= sign
    
    # int conversion 
    int_min, int_max = -2 **31, 2**31 - 1
    
    # clamping 
    if res < int_min:
        return int_min
    elif res > int_max:
        return int_max

    return res        
    
    
# print(my_atoi())



# power exponentiation
def pow_x_n():
    
    x = 3
    n = 1700
    res = x ** n 
    
    return res

print(pow_x_n())




