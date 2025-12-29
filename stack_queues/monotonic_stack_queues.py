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
            if popped != idx:
               res[popped] = s[idx]
            
        
        if i < n:
            stack.append(idx)
            
    return res

# print(small_element([1,6,3,9]))
        
        
        
# next small element  
def next_small_elem(s):
    
    stack = []
    n = len(s)
    res = [-1] * n
    
    for i in range(2 * n-1, -1, -1):
        idx = i % n
        
        while stack and stack[-1] >= s[idx]:
            stack.pop()
            
        if stack:
            if i < n:
                res[idx] = stack[-1]
            
        stack.append(s[idx])
            
    return res

# print(next_small_elem([1,6,3,9]))


def prev_small(s):
    
    stack = []
    n = len(s)
    res = [-1] * n
    
    for i in range(n):
        while stack and stack[-1] >= s[i]:
            stack.pop()
            
        if stack:
            res[i] = stack[-1]
        else:
            res[i] = -1
            
        stack.append(s[i])
        
    return res 

# print(prev_small([1, 6, 3, 9]))


# no. of NGE to the right 
def number_NGE(arr):
    
    n = len(arr)
    res = [0] * n
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] > arr[i]:
                res[i] += 1
       
    return res

# print(number_NGE([3, 4, 2, 7, 5, 8, 10, 6])) 




# trapping of rain water - find max on both left and right til point i [LC - 42]
def rain_water(height): # brute force approach 
    
    n = len(height)
    total = 0
    
    for i in range(n):
        
        left_max = 0
        for j in range(i):
            if height[j] > left_max:
                left_max = height[j]
                
        right_max = 0
        for j in range(i+1, n):
            if height[j] > right_max:
                right_max = height[j]
                
        water = min(left_max, right_max) - height[i]
        
        if water > 0:
            total += water
            
    return total

# print(rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
            


# trapping rain water - [LC - 42] 
def rain_water_optimal(height):
    
        n = len(height)
        total = 0
        
        if n == 0:
            return 0
        
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(n):
            left_max[i] = max(left_max[i-1], height[i])
                
        right_max = [0] * n
        right_max[n-1] = height[n-1]
        for i in reversed(range(n-1)):
            right_max[i] = max(right_max[i+1], height[i])
                
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                total += water
            
        return total
    
# print(rain_water_optimal([4,2,0,3,2,5]))




# - - - [kadane's algorithm]
def sum_subarray():   # maximum subarray
    arr = [3,-1,2,4]
    
    current = arr[0]
    min_sum = arr[0]
      
    for i in arr[1:]:
       current = min(i, current + i)
       min_sum = min(min_sum, current)
       
    return min_sum 

# print(sum_subarray())    

# minimum subarray
def maxSum_subarray(arr):
    curr = arr[0]
    max_sum = arr[0]
    n = len(arr)
    
    for i in range(1, n):
        curr = max(arr[i], curr + arr[i])
        max_sum = max(max_sum, curr)
        
    return max_sum

print(maxSum_subarray([3,1,2,4]))



# subarray of the minimums - - brute force approach   
def subarray_mins(arr):
    
    n = len(arr)
    res = 0
    
    for i in range(n):
        for j in range(i, n):
           sub = arr[i:j+1]
           res += min(sub)
            
    return res

# print(subarray_mins([3,1,2,4]))


# subarray of minimums - - - optimal approach
def subarr_mins(arr):
    
    n = len(arr)
    MOD = 10**9 + 7
    
    # find left smaller element 
    stack = [] 
    left = [0] * n
    
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
            
        if not stack:
            left[i] = i + 1
        else:
            left[i] = i - stack[-1]
            
        stack.append(i)
        
    
    # find right smaller elements 
    stack = []
    right = [0] * n
    
    for i in range(n-1, -1, -1):
        
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
            
        if not stack:
            right[i] = n - i
        else:
            right[i] = stack[-1] - i
            
        stack.append(i)
        
        
    # calculate total 
    total = 0
    for i in range(n):
        total += arr[i] * left[i] * right[i]
        
    return total % MOD

# print(subarr_mins([3, 1, 2, 4]))



# asteriod collision position - brute force  
def prevent_collision(arr):    
    stack = []
    
    i = 0
    
    for i in arr:
        while stack and stack[-1] > 0 and i < 0:
           if stack[-1] < abs(i):
               stack.pop()
               continue
           elif stack[-1] == abs(i):
                stack.pop()
                break
           else:
               break 
           
        else:
            stack.append(i)
            
    return stack

# print(prevent_collision([5,10,-5]))


