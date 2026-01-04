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


            

