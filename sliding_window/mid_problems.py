""" SLIDING WINDOW MIDS WILL BE SOLVED HERE 
 - - - GIVEN QUESTIONS ARE 8 IN TOTAL 
"""  


# longest non-repeating substring - - - O(n) --- [lc - 3]
# variable based sliding window (always uses while loop)
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
        
        
        
# fruit into baskets - - [LC - 904]
def fruit_baskets(arr):
    
    n = len(arr)
    left = 0
    max_len = 0
    basket = {}  # in hashmap 
    
    
    for right in range(n):
        
        # add fruits
        if arr[right] in basket:
            basket[arr[right]] += 1
        else:
            basket[arr[right]] = 1
            
        # if limit exceeds 
        while len(basket) > 2:
            basket[arr[right]] -= 1
            if basket[arr[left]] == 0:
               del basket[arr[left]]
            left += 1
            
        max_len = max(max_len, right-left+1) 
    
    return max_len
            
            
# print(fruit_baskets([1,2,1]))



# lc - 424
def longest_repeat_char_replace(s, k):
    
    n = len(s)
    left = 0
    max_len = 0
    store = {} 
    
    for right in range(n):
        if s[right] in store:
           store[s[right]] += 1
        else:
            store[s[right]] = 1
            
        window_len = right-left+1
        max_freq = max(store.values())
        
        if window_len - max_freq > k:
            store[s[left]] -= 1
            left += 1
            
        max_len = max(max_len, window_len)
    return max_len

# print(longest_repeat_char_replace("ABAB", 2))




# Lc - 930  [not a slding window problem]
def binary_subarray_sum(arr, k):
    
    mapps = {0:1}
    current_sum = 0
    cnt = 0
    
    for i in arr:
        current_sum += i
        
        if (current_sum - k) in mapps:
            cnt += mapps[current_sum - k]
        
        if current_sum in mapps:
            mapps[current_sum] += 1
        else:
            mapps[current_sum] = 1
            
    return cnt
    
# print(binary_subarray_sum([1,0,1,0,1], 2))



# lc - 1248 [not a sliding window prblem]
def coun_nums_subarrs(arr, k):
    
    convert = []
    
    for i in arr:
        if i % 2 == 1:
            convert.append(1)
        else:
            convert.append(0)
            
            
            
    maps = {0:1}
    curr_sum = 0
    cnt = 0
    
    for x in convert:
        curr_sum += x
        
        if (curr_sum - k) in maps:
            cnt += maps[curr_sum - k]
            
        if curr_sum in maps:
            maps[curr_sum] += 1
        else:
            maps[curr_sum] = 1
            
    return cnt 

# print(coun_nums_subarrs([1,1,2,1,1], 3))



# lc - 525
def contiguos_arr(arr):
    
    convert = []
    
    for i in arr:
        if i == 0:
            convert.append(-1)
        else:
            convert.append(+1)
            
    maxlen = 0
    maps = {0: -1}
    curr = 0
    n = len(convert)
            
    for x in range(n):  
        curr += convert[x]
          
        if curr in maps:
            length = x - maps[curr]
            maxlen = max(maxlen, length)
        else:
            maps[curr] = x
           
    return maxlen

# print(contiguos_arr([0,1]))
             
             
             

