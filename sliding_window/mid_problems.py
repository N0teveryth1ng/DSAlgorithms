""" SLIDING WINDOW MIDS WILL BE SOLVED HERE 
 - - - GIVEN QUESTIONS ARE 8 IN TOTAL 
"""  


# longest non-repeating substring - - - O(n) --- [lc - 3]
# variable based sliding window (always uses while )
def non_repeat(s):
    
    n = len(s)
    sett = set()
    res = 0
    left = 0
    
    for right in range(n):
        while s[right] in sett:
           sett.remove(s[left])
           left += 1 
        sett.add(s[right])
        res = max(res, right-left+1)
    return res 

# print(non_repeat("abcabcbb")) 
            

    
# max average --- [LC - 643]
# fixed size window 
def max_avg(s, k):
    
    current_sum = sum(s[:k])
    max_sum = current_sum 
    n = len(s)
    
    for i in range(n - k): 
        current_sum = current_sum - s[i] + s[i+k]
        max_sum = max(max_sum, current_sum)
        
    return max_sum/k 

# print(max_avg([1,12,-5,-6,50,3], 4))
    
    
    
# LC - 1004
def max_consec_III(arr, k):
    n = len(arr)
    left = 0
    max_len = 0
    zero_cnt = 0
    
    for right in range(n):
        if arr[right] == 0:
            zero_cnt += 1
            
        while zero_cnt > k:
            if arr[left] == 0:
                zero_cnt -= 1
            left += 1
        
        max_len = max(max_len, right-left+1)
        
    return max_len

# print(max_consec_III([1,1,1,0,0,0,1,1,1,1,0], 2))
        
        
        
# fruit into baskets
def fruit_baskets():
    
    