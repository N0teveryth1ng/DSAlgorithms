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



# [sort colors in LC - 0,1,2]
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
            
                       
