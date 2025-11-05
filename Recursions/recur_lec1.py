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
    

# generate all binary strings - - - - - 
def generate_binary_strs(n, current=""):
    
    if len(current) == n:
        print(current)
        return
    
    generate_binary_strs(n, current + "0")
    generate_binary_strs(n, current + "1")
    
# print(generate_binary_strs(3))


# generate parenthese
""" output  - ['((()))', '(()())', '(())()', '()(())', '()()()'] """ 
def generate_pars(n):
    store = []
    def backtrack(current, open, close):
        if len(current) == n * 2:
            store.append(current)
            return
        
        if open < n:
            backtrack(current + "(", open + 1, close)
            
        if close < open:
            backtrack(current + ")", open, close + 1)
            
    backtrack("", 0,0)
    return store

# print(generate_pars(3))
    

    
# print all the subsets
    

    # MIND MAP for the suubsets
    
    #                       []
    #                 /             \
    #              [1]               []
    #            /    \            /    \
    #        [1,2]    [1]        [2]      []
    #        /   \    / \        / \      / \
    #  [1,2,3][1,2] [1,3][1]  [2,3] [2]   [3] []
    
    
def subsets(nums):
    res = []
    subset = []
    def dfs(i):
        if i == len(nums):
           res.append(subset.copy())
           return
       
        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)
        
        # decision to NOT include nums[i]
        subset.pop()
        dfs(i + 1)
        
    dfs(0)
    return res  
            

# count the subsequence with sum K - - - - - - -
def subsets_sum_k(i, nums, current, target, current_sum):
        if i == len(nums):
            if current == target:
               print(current)
            return 
        
        # choice 1 - include nums[i] 
        current.append(nums[i])
        subsets_sum_k(i+1, nums, current, target, current_sum + 1)
        
        # choice 2 - NOT include nums[i]
        current.pop()
        subsets_sum_k(i+1, nums, current, target, current_sum)
        
        
        
# check if there exists a subsequence with sum k
def exists_subsets_k_sum(i, nums, target, current_sum):
    if i  == len(nums):
       return current_sum == target
   
    include = exists_subsets_k_sum(i+1, nums, target, current_sum + nums[i])
    
    if include:
        return True
    
    exclude = exists_subsets_k_sum(i+1, nums, target, current_sum)   
    return exclude

nums = [3, 1, 5, 9, 12]
target = 9
# print(exists_subsets_k_sum(0, nums, target, 0))
    
    
    
# combination sum 
def combination_sum():
    
    
        
    
    
    
