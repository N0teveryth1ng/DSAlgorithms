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
def fruit_baskets(arr, k):
    
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
        while len(basket) > k:
            basket[arr[left]] -= 1
            if basket[arr[left]] == 0:
               del basket[arr[left]]
            left += 1
            
        max_len = max(max_len, right-left+1) 
    
    return max_len
            
            
# print(fruit_baskets([1,2,1], 2))




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
             
             
             

# lc - 209 - - 
def min_size_subarr(arr, k):
    
    n = len(arr)
    left = 0
    min_len = float('inf')
    current_sum = 0
    
    for right in range(n):     
        current_sum += arr[right]
        
        while current_sum >= k:
            min_len = min(min_len, right-left+1)
            current_sum -= arr[left]
            left += 1
            
    return 0 if min_len == float('inf') else min_len
            
# print(min_size_subarr([2,3,1,2,4,3], 7))
    
    
         
         
         
# lc - 713 [ subarr product < k]
def subarr_prod_k(arr, k):
            
    left = 0
    res = 0 
    prod = 1
    n = len(arr)
    
    for right in range(n):
        prod *= arr[right]
        
        while prod >= k:
            prod /= arr[left]
            left += 1
            
        res += (right-left+1)
    return res 

# print(subarr_prod_k([10,5,2,6], 100))



# lc - 2962 [Count Subarrays Where Max Element Appears at Least K Times]
def cnt_subarr(arr, k):
    
    left = 0
    maxlen = 0
    cnt = 0
    maps = {}
    
    n = len(arr)
    
    for right in range(n):
        if arr[right] in maps:
            maps[arr[right]] += 1
        else:
            maps[arr[right]] = 1
            
            
        maxlen = max(maxlen, maps[arr[right]])    
            
        # expand window
        while maxlen >= k:
            cnt += n - right
            maps[arr[left]] -= 1
            
            if maps[arr[right]] + 1 == maxlen:
                maxlen = max(maps.values())
            
            left += 1    
            
    return cnt 
        
# print(cnt_subarr([1,3,2,3,3], 2))



# Maximum Points You Can Obtain from Cards [lc - 1423]
def maxscore(arr, k):
    
    n = len(arr)
    total_sum = sum(arr)
    
    if k == n:
        return total_sum
     
    window_size = n - k
    curr_sum = sum(arr[:window_size])
    min_sum = curr_sum
    
    # move window 
    for i in range(window_size, n):
        curr_sum = curr_sum - arr[i - window_size] + arr[i]
        min_sum = min(min_sum, curr_sum)
        
    return total_sum -  min_sum
        
# print(maxscore([1,2,3,4,5,6,1], 3))
    
    
    

#  longest substring with atmost k distinct chars - [LC - 340]
# same as LC - 904 just for strings
def lc_340(s, k):
    
    n = len(s)
    
    left = 0
    maxlen = 0
    mapps = {}
    
    for right in range(n):
        
        # if exists in mapps
        if s[right] in mapps:
            mapps[s[right]] += 1
        else:
            mapps[s[right]] = 1
            
        # shrink window when size > k  
        while len(mapps) > k:
            mapps[s[left]] -= 1
            if mapps[s[left]] == 0:
                del mapps[s[left]]
            left += 1
                        
        maxlen = max(maxlen, right-left+1)
        
    return maxlen

# print(lc_340("eceba", 2))
    



# LC - 992 [subarrs with k different values ]
class sol:
    def lc_992(self, arr, k):
        left = 0
        cnt = 0
        mapps = {}
        n = len(arr)
        
        # if exists on map or not 
        for right in range(n):
            if arr[right] in mapps:
                mapps[arr[right]] += 1
            else:
                mapps[arr[right]] = 1
                
            # window check 
            while len(mapps) > k:
                mapps[arr[left]] -= 1
                if mapps[arr[left]] == 0:
                    del mapps[arr[left]]
                left += 1
                
            cnt += (right-left+1)
            
        return cnt
        
        
    def k_distincts(self, arr, k):
        return self.lc_992(arr, k) - self.lc_992(arr, k-1) 



# minimim window substr - [LC - 76]
def lc_76(s, t):
    
    n = len(s)
    left = 0
    min_len = 0
    mapps = {}
    count_sum =  0
    
    for right in range(n):
        count_sum += s[right]
                
        # window shrink
        while count_sum >= t:
            min_len = min(min_len, right-left+1)
            count_sum -= s[left]
            left += 1
        
    return min_len