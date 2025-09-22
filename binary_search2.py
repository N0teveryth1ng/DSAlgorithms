# binary search part 2


# find the sqr root of an integer
def sqrt():
    
    n = 37
    ans = 0
    
    for i in range(n):
        if i*i <= n:
           ans = i
        else:
            break
    return ans
    
# print(sqrt()) 
    
    
#   - - - -  binary approach for square root 
def optimal():

    n = 37
    ans = 0
        
    low , high = 1, n
    
    while low <= high:
        mid = (low + high) // 2 
        
        if mid * mid <= n:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans

# print(optimal())


# find the root of the Nth integer
def nth_root(A, N):
    if A == 0: return 0
    if N == 1: return A
    
    low, high = 1, A
    while low <= high:
        mid = (low + high) // 2
        power = mid ** N
        if power == A:
            return mid
        elif power < A:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# print(nth_root(25, 2))



# koko eating bananas
import math

def koko_banana():
    
    piles = [3,6,7,11]
    h = 8
    low, high = 0, max(piles) 
    res = high
    
    while low <= high:
        
        mid = (low + high) // 2 
        hours = 0
        for p in piles:
            hours += math.ceil(p / mid)
        
        if hours <= h:
            res = min(res, mid)
            high = mid - 1
        else:
            low = mid + 1
            
    return res


# print(koko_banana())


    
# Minimum Number of Days to Make m Bouquets  
def bloomDay():
    
   arr = [1,10,3,10,2]
   m = 3
   k = 1             
   n = len(arr)
   
   if m * n > n:
      return -1
   
   low, high = 1, max(arr)
   
   while low <= high:
        
        mid = (low + high) // 2   
        blooms = 0
        consec = 0
        
        for i in arr:
            if i <= mid:
                consec += 1     
                
                if consec == k:
                    blooms += 1
                    consec = 0
            else:
              consec = 0
        
        if blooms >= m:
            high = mid - 1
        else:
            low = mid + 1
            
   return low

# print(bloomDay())    



# smallest divisor to a threshold
# brute fore approach 
def divisor():
    
    nums = [1,2,5,9]
    threshold = 6
    
    n = len(nums)
        
    for div in range(1, max(nums) + 1):    
        x = 0
        for i in nums:
            x += math.ceil(i/div) 
            
        if x <= threshold:
            return x
            
    
# print(divisor())


# optimal approach - - - - find the smallest divisor on a threshold
def parent():
    
    nums = [1,2,5,9]
    threshold = 6
    
    low, high = 1, max(nums) + 1
    
    while low <= high:
        
        mid = (low + high) // 2
        total = 0
        
        for num in nums:
            total += (num + mid - 1) // mid
            
        if total <= threshold:
            high = mid - 1
        else:
            low = mid + 1
            
    return low

# print(parent())



# least capacity to ship packages 
def ship():
    
    Weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5     
    low, high = max(Weights), sum(Weights)
    
    while low <= high:
        
        mid = (low + high) // 2
        res = 0
        days_need = 1
        
        # simulate shipping with current capacity
        for i in Weights:
            if res + i <= mid:
                res += i
            else:
                days_need += 1
                res = i
            
        # if the capacity works
        if days_need <= days:
            high = mid - 1
        else:
            low = mid + 1
                
    return low
    
# print(ship())


# brute force method  ---   kth missing positive element 
def kth_elem():    
    arr = [2,3,4,7,11]
    k = 5
    
    for i in range(len(arr) - 1):
        if arr[i] < k:
            k += 1
        else:
            break
    
    return k
        
# print(kth_elem())

#   - - -  kth element find - -  with optimal approach
def kth_optimal():
    
    arr = [2,3,4,7,11]
    k = 5
    
    n = len(arr)
    low, high = 0, n-1
    
    while low <= high:
        mid = (low + high) // 2
        
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
            
    return low + k


# print(kth_optimal())



# number of agggresive cows  - - - - each cows should have minimum gap before placing 
def cows():
    
    arr = [2,5,8,10]
    k = 3
    arr.sort()
    n = len(arr)
    
    low, high = 1, max(arr) - min(arr)
    res = 0
    
    while low <= high:
        
        mid = (low + high) // 2
        count = 1
        last_pos = arr[0]
        
        for i in range(1, n):
            if arr[i] - last_pos >= mid:
                count += 1
                last_pos = arr[i]
                if count == k:
                    break
                
        if count >= k:
            res = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return res

# print(cows())
    



# allocate books - -  each student should have 1 book atleast 
def allocate():
    
    arr = [25, 46, 28, 49, 24]
    student = 4
    low, high = max(arr), sum(arr)
    result = high
     
    #  greedy 
    while low <= high:
        mid = (low + high) // 2
        required, pages = 1, 0
        
        for i in arr:
            if pages + i > mid:
                required += 1
                pages = i
            else:
                pages = i            
            
        
        if required <= student:
            result = mid
            high = mid - 1
        else:
            low = mid + 1
        
    return result 

# print(allocate())
        
        
# split arrays into the largest sum 
def largest_sum():
    
    nums = [7,2,5,10,8]
    k = 2
    
    low, high = max(nums), sum(nums)
    res = high 
    
    # can we split nums into <= k subarrays with max sum <= k
    def can_split(mid):
        count, curr_sum =  1, 0
        for i in nums:
            if curr_sum + i > mid:
                count += 1
                curr_sum = i
                if count > k:
                    return False
                
            else:
                curr_sum += i
        return True
            
        
    # binary search 
    while low <= high:        
        mid = (low + high) // 2
        if can_split(mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
                    
    return res

# print(largest_sum())




#  - - - - - - -    PROBLEMATIC ONE  - - - - - - - -  -
# minimise max distance between gas stations or 2 points 
# given = [1,7] , k = 2
# approach = [1, 3, 5, 7] ----- reduced distance by 2 points 
def gas_station():
    
    arr = [1,7]
    k = 2
    n = len(arr)
    max_sec = -1
    max_ind = -1
    
    for i in range(n-1):
        
        diff = arr[i+1] - arr[i]
        sec_len = (diff/ arr[i] + 1)
        
        if sec_len > max_sec:
           max_sec = sec_len
           max_ind = i
        
    max_ind += 1
    
    max_ans = -1
    for i in range(n-1):
         diff = arr[i+1] - arr[i]
         sec_len = (diff/arr[i] + 1)
         max_ans = max(max_ans, sec_len)
         
    return max_ans   

        
# print(gas_station())
        
        




# - - - - -  median of two sorted arrays
# approach -- As the arr is already sorted we first merge it in sorted order and then implement median find - 

# brute force - external storage 
def median_sorted():
    
    arr1 = [1,2] 
    arr2 = [3]
    
    n1 = len(arr1)
    n2 = len(arr2)
    i, j = 0, 0
    arr3 = []
    
    # merge sort
    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
        
    while i < n1:
        arr3.append(arr1[i])
        i += 1
        
    while j < n2:
        arr3.append(arr2[j])
        j += 1
        
    # find median
    n = n1 + n2
    if n % 2 == 1:
        return arr3[n//2]
    
    
# print(median_sorted())


# optimal approach - median of 2 sorted arrays 
def median_approach():
    
    nums1 = [1,3]
    nums2 = [2]
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    m,n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2
    
    left, right = 0, m
    while left <= right:
        i = (left + right) // 2    #for parting arr1 
        j = half - i               #for parting arr2
        
        # get the border values
        left1 = nums1[i-1] if i > 0 else float("-inf")
        right1 = nums1[i] if i < m else float("inf")
        
        left2 = nums2[j-1] if j > 0 else float("-inf")
        right2 = nums2[j] if j < n else float("inf")
        
        # check if partition is correct or not 
        if left1 <= right2 and left2 <= right1:
            if total % 2 == 1:
                return max(left1, left2)
            return (max(left1, left2) + min(right1, right2)) // 2.0
        elif left1 > right2:
            right = i - 1
        else:
            left = i + 1
            

# print(median_approach())



# find the K-th elem of two sorted array
def kth_elem():
    
    nums1 = [1,3]
    nums2 = [2]
    k = 2
    
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
        
    m,n = len(nums1), len(nums2)
    
    left, right = 0, m
        
    while left <= right:
        i = (left + right) // 2
        j = k - i
        
        # parting in arrays
        left1 = nums1[i-1] if i > 0 else float("-inf") 
        right1 = nums1[i] if i < m else float("inf")
        
        left2 = nums2[j-1] if j > 0 else float("-inf")
        right2 = nums2[j] if j < n else float("inf")
        
        
        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)
        
        elif left1 > right2:
            right = i - 1
        else:
            left = i + 1
            
            
# print(kth_elem())        

       
       

            