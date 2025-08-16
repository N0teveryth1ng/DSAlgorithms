# Medium problem solving array 

#  - - - - - - - 2 SUM (brute force method)
def twosum():
    arr = [5,2,5,6,4]
    target = 10
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            
            if arr[i] + arr[j] == target:
                return i,j
    return []
        
# print(twosum())    


def test(): # - - - - - - - - optimal apppaoch
    arr = [2,5,2,4]
    target = 9
    hash_map = {}
   
    for i in range(len(arr)):
       completed = target - i
       if completed in hash_map:
          return hash_map[completed],i
      
       hash_map[arr[i]] = i
        
# print(test())



# [sort colors in LC - 0,1,2] - - - [DNF algorithm]
def array():
    arr = [2,2,2,2,1,1,1,1,0,0,0,0]
    
    low = 0
    mid = 0
    high = len(arr) - 1
 
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1 
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
            
    return arr

# print(array())




# majority elemnt - - - moore's algo method 
# count the default num if new nums appears reduce count by 1. 
# after reaching 0 starts from new num and increment to 1 count.    

def majority():
    arr = [2,2,2,3,3,1,2,2]
    n = len(arr)
    
    candidates = None
    count = 0
    
    for i in range(n):    
        if count == 0:
            candidates = i
        if i == candidates:
            count += 1
        else:
            count -= i
    
    return candidates

# print(majority())
            
                   
                    
# kadane's algo - - - [contingeous subarray]
def kadanes():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    current_sum = 0
    max_sum = float('-inf')
    
    for i in arr:
        current_sum = max(i, current_sum + i)
        
        max_sum = max(max_sum, current_sum)
        
    return max_sum
        
# print(kadanes())

def simplest(arr):
    
    current_sum = arr[0]
    max_sum = arr[0]
    
    for i in arr[1:]:
        
        current_sum = max(i, current_sum + i)
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# print(simplest([-2,1,-3,4,-1,2,1,-5,4]))


# DP on stocks

def stocks():
    
    arr = [7,1,5,3,6,4]
    n = len(arr)
    
    min_price = arr[0]
    max_profit = 0
    
    for i in range(1,n):
        
        cost = arr[i] - min_price
        max_profit = max(cost, max_profit)
        
        min_price = min(min_price, arr[i])
         
    return max_profit

# print(stocks())


def test():   # MORE better way to undertand stock DP
    
    arr = [7,1,5,3,6,4]
    n = len(arr)
    
    min_price = arr[0]  # assume 1st elem as lowest
    max_profit = 0
    
    # find the lowest price
    for i in range(n):
       if arr[i] < min_price:
           min_price = arr[i]
           
       profit = arr[i] - min_price   # profit = sell price - buy price     
        
        # if find better price then sell it
       if profit > max_profit:
           max_profit = profit
           
    return max_profit

# print(test()) 


# most optimal intepretation - Rearrange the array in alternating positive and negative items
def rearrange():
    arr = [1, 2, 3, -4, -1, -4]
    n = len(arr)
    res = [0] * n
    
    i,j = 0,1
    
    for k in range(n):
        if arr[k] > 0 and i < n:
            res[i] = arr[k]
            i += 2
        else:
            res[j] = arr[k]
            j += 2
            
    return res


# print(rearrange())



#  NEXT PERMUTATION - - longest prefix sum 
# s1 - find the pivot
# s2 - find the greater digit elem than pivt
# s3 - swap the elems with the pivot
# s4 - reverse the suffix and miantain rhe reminaings rest
 
def permutation():
    arr = [2,1,5,4,3,0,0]
    
    pivot = -1
    n = len(arr)
    
    for i in range(n-2,-1,-1):
       if arr[i] < arr[i+1]:
           pivot = i
           break
       
    if pivot == -1:
        arr.reverse()
        return arr
       
       
    for j in range(n-1,pivot,-1):
        if arr[j] > pivot:
            arr[pivot], arr[j] = arr[j], arr[pivot]
            break
        
    
    arr[pivot+1:] = reversed(arr[pivot+1:])
    
    return arr


# print(permutation())




# LEADER elem -- Find the leader elems of an array
# - traverse from the right of the loop

def leader():
    arr = [16, 17, 4, 3, 5, 2]
    
    n = len(arr)
    leader_nums = []
    max_right = arr[-1]
    leader_nums.append(max_right)
    
    for j in range(n-2,-1,-1):
        if arr[j] > max_right:
           leader_nums.append(arr[j]) 
           max_right = arr[j]
       
    
    leader_nums.reverse()    
    return leader_nums

# print(leader())


# LONGEST consecutive -- brute force application
# Parse thrugh each and every elemnt of the array
# maxing the last of the longest
def long_consec():
    arr = [100,4,200,1,3,2]
    n = len(arr)
    
    longest = 1
    
    for i in range(n):
        x = arr[i]
        cnt = 1
        
        while x + 1 in arr:
                x += 1
                cnt += 1
                
        longest = max(longest, cnt)
        
    return longest

# print(long_consec())
                
                
# optimal approach  - - 
# instead of parsing every elem each at a time
# use set for each time parsing & maxing the last of the longest
def longest_consec():
    
    arr = [100,4,200,1,3,2]
    num_set = set(arr)
    
    longest = 0
    
    for i in num_set:
         
        if i - 1 in num_set:
            current_num = i
            count = 1    
     
            while current_num + 1 in num_set:
                current_num += 1
                count += 1
                
            longest = max(longest, count)
            
    return longest


# print(longest_consec())    
        
        
        
# Set matrix 0's - - -

# - mark all the 0s first in rows and cols
# - mark very non 0's to -1 both row and col level
# - lastly turn evry -1 into 0s now. AT row and cols levle

def matrix():
# brute force approach     
    arr =  [[1,1,1],[1,0,1],[1,1,1]]
    rows = len(arr)
    cols = len(arr[0])
    
    zero_rows = set()
    zero_cols = set()
    
    # mark all the 0s
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
                
    # turn non-0s in -1 at rows level
    for i in zero_rows:
      for j in range(cols):
        if arr[i][j] != 0:
            arr[i][j] = -1
            
                
    # turn non-0s in -1 at cols level
    for j in zero_cols:
      for i in range(rows):
        if arr[i][j] != 0:
            arr[i][j] = -1
            
            
    # now turn all the -1 into 0s
    for i in range(rows):
        for j in range(cols):
            if arr[i][j] == -1:
                arr[i][j] = 0
                
    
    return arr
                
# print(matrix())

# optimla approach
#  - keep track of the 0s 
def matrix_optimal():
    
    arr = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    
    rows, cols = len(arr), len(arr[0])
    
    rowZero = False
    
    for i in range(rows):
        if arr[i][0] == 0:
            rowZero = True
        
        for j in range(1,cols):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0
                    
