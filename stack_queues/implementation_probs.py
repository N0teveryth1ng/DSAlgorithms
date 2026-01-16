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







#  LRU cache
# method:  
# 1. hashMap to find address 
# 2. DLL for inseting/removing

class DLL_LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.head = None
        self.tail = None
        
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val   
            self.prev = None
            self.next = None
    
    def insert(self, node):
        node.next = self.head
        node.prev = None
        
        if self.head:
            self.head.prev = node
        self.head = node
        
        if not self.tail:
            self.tail = node
        
    
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next 
            
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
            
        
        node.prev = None
        node.next = None
        
        
    
    def get(self, key):
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        return -1
        
        
    def put(self, key, value):
        # updating first -- insrt the new elem in prev index
        if key in self.hash_map:
            node = self.hash_map[key]
            node.val = value
            
            self.remove(node)   #remove the old val 
            self.insert(node)   #insert from front for updation  
            
            
        # insertion - insert a new elem at new index 
        else:
            if len(self.hash_map) == self.capacity:
               lru_cache = self.tail
               self.remove(lru_cache)
               del self.hash_map[lru_cache.key]
        
            # create new node with key value pairs 
            new_node = self.Node(key, value)
            self.insert(new_node)
            self.hash_map[key] = new_node
            
            
            
            
cache = DLL_LRU(2)
cache.put(1, 10)      # [1:10]
cache.put(2, 20)      # [2:20, 1:10]
print(cache.get(1))   # 10 → moves 1 to front: [1:10, 2:20]
cache.put(3, 30)      # evicts 2 → [3:30, 1:10]
print(cache.get(2))   # -1 (evicted)
print(cache.get(1))   # 10


# LFU IS STILL LEFT HOPE I CAN WATCH IT BEFORE THE INTERVEW