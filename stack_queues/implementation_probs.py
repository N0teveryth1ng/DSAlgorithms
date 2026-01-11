# Final stretch to stack and queue concepts 
# brute force method
from collections import deque


# sliding window maximum 
def sliding_window():
    
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    n = len(arr)
    res = []
    
    for i in range(n-k + 1):
        maxi = arr[i]
        for j in range(i, i + k):
           maxi = max(maxi, arr[j])
        res.append(maxi)
        
    return res

# print(sliding_window())




# optimal  method  - - - - sliding window
def sliding_optimal_max(arr, k):
    n = len(arr)
    
    dq = deque()
    stack = []
    
    for i in range(n):
      
        # 
        if dq and dq[0] <= i - k:
            dq.popleft()
      
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
            
        dq.append(i)
        
        if i >= k - 1:
            stack.append(arr[dq[0]])
            
    return stack
        
# print(sliding_optimal_max([1,3,-1,-3,5,3,6,7], 3))



# Plus one - [POTD] 
def plus_one(arr):
    
    n = len(arr)
    for i in range(n-1, -1, -1):
        if arr[i] < 9:
            arr[i] += 1
            return arr  
        else:
            arr[i] = 0
            
    return [1] + arr

# print(plus_one([1,2,3]))



# online stock span - brute idea  
def stock_span(arr):
    
    n = len(arr)
    span = [1] * n
    
    for i in range(n):
        cnt = 0
        for j in range(i-1, -1, -1):
            if arr[i] >= arr[j]:
                cnt += 1
            else:
                break
            
        span[i] = cnt
            
    return span

# print(stock_span([100 ,80 ,60 ,70 ,60 ,75 ,85])) 
        
        
# stock span [optimal sol] - - single price list based 
# 
def optimal_sol(arr):
    
    n = len(arr)
    res = [0] * n
    stack = [] 
    
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
            
        if stack:
            res[i] = i - stack[-1]
        else:
            res[i] = i + 1
            
        stack.append(i)
            
    return res

# print(optimal_sol([100 ,80 ,60 ,70 ,60 ,75 ,85]))
              
              
              
# class order based to handle unexpected price lists
class stock:
    def __init__(self):
        self.stack = []
        self.day_index = 0
    
    def stock_price(self, arr):
        
        while self.stack and self.stack[-1][0] <= arr:
              self.stack.pop()
              
        if self.stack:
            span = self.day_index - self.stack[-1][0]
        else:
            span = self.day_index + 1
            
        self.stack.append((arr, self.day_index))
        self.day_index += 1
        
        return span
    
spanner = stock()
# print(spanner.stock_price(80)) 



# stock spanning problem - - -  
def stock_planner(arr):
    
    n = len(arr)
    res = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
            
        if stack:
            res[i] = i - stack[-1]
        else:
            res[i] = i + 1
            
        stack.append(i)
        
    return res 

# print(stock_planner([100, 80, 60, 70, 60, 75, 85]))



# 
    