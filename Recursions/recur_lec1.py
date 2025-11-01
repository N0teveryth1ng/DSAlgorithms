# We will be continuing with recursions and its problems in order to get a strong hold of it

# My ATOI - 
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

# print(pow_x_n())


# pow(x,n) - - - - leetcode 50 - - [ Got fucked while understanding and solving it  ]
def pow_X_N(x, n):
    def helper(x , n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = helper(x, n // 2)
        res = res * res
        return x * res if n % 2 else res
    
    res = helper(x, abs(n))
    return res if n >= 0 else 1 / res

# print(pow_X_N(2, -3))



# count good numbers ( odd-even sets)
MOD = 10**9 + 1
def predict_modPow(x,n):
    
    if n == 0:
        return 1
    
    half = predict_modPow(x , n//2)
    half = (half * half) % MOD
    
    if n % 2:
        half = (half * x) % MOD
        
    return half

def count_good_nums(n):
    
    even_pos = (n + 1) // 2
    odd_pos = n // 2
    
    even_part = predict_modPow(5, even_pos)
    odd_part = predict_modPow(4, odd_pos)
    
    return (even_part * odd_part) % MOD

# print(count_good_nums(4))



# sort a stack using recursion
#  - - -  1. insert vals after sorting in stack in insert_sorted()
#         2. sort stack after overall vals has been inserted in sort_stack()

def insert_sorted(stack, value):
    
    if not stack and value > stack[-1]:
        stack.append(value)
        return
    
    temp = stack.pop()
    insert_sorted(stack, temp)
    stack.append(temp)
    
def sort_stack(stack):
    
    if len(stack) <= 1:
        return
    
    temp = stack.pop()
    sort_stack(stack)
    insert_sorted(stack, temp)
    
    
# reverse a stack using recursion - - - - - - - -  -  same a 
def insert_at_bottom(stack, value):
    
    if not stack:
        stack.append(value)
        return
    
    temp = stack.pop()
    insert_at_bottom(stack, value)
    stack.append(temp)
    
def rev_stack(stack):
    
    if not stack > 1:
        return
    
    temp = stack.pop()
    rev_stack(stack)
    insert_at_bottom(stack, temp)
    
    