# Hard array problem solving 


# PASCAL TRIANGLE - - - - 
# add the below row based on above elems  - - - [ nCr FORMULA CONCEPT IS NOT CLEAR WELL TO ME]

def pascal():
    
    n = 5
    triangle = [[1]]
    
    for i in range(1,n):
        prev_row = triangle[-1]
        new_row = [1]
        
        for j in range(len(prev_row) - 1):
            new_row.append(prev_row[j] + prev_row[j+1])
            
            
        new_row.append(1)
        triangle.append(new_row)
        
    return triangle


# print(pascal())
        
        

# MAJORITY ELEMENT II - n/3  - - - [the max elems can appear at max 2]
# example - arr[1,1,1,3,3,2,2,2] ---> ans[1,2]

#  - - - - - - - Extended moore's algorithm
def majority2():
    
    arr = [1,1,1,3,3,2,2,2]
    
    n = len(arr)
    count1, count2 = 0, 0
    candid1, candid2 = None, None
    
    for num in arr:
        if num == candid1:
           count1 += 1 
        elif num == candid2:
            count2 += 1
        elif count1 == 0:
            candid1, count1 = num, 1
        elif count2 == 0:
            candid2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1
            
    res = []
    for candidate in [candid1, candid2]:
        if candidate is not None and arr.count(candidate) > n//3:
           res.append(candidate)            
            
    return res

# print(majority2())



  
# 2 Sum part - 2  - - - - sorted list of array [ previous 2 sum easy ]
def twoSum_2():
    
    arr = [2,7,11,15]
    target = 9
    left, right = 0, len(arr) - 1
    
    while left < right:
        
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
            
    return []

# print(twoSum_2())
    
    
    
# 3 sum - - - [naive approach]
def three_sum(nums):
    
    
    res = set()
    
    n = len(nums)
    for i in range(n):
        for j in range(i+1  , n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                   triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                   res.add(triplet)         
                        
    return res
              
              
# print(three_sum([-1,0,1,2,-1,-4]))


# 3 sum best approach 
def optimal_3sum():
    
    arr = [-1,0,1,2,-1,-4]
    arr.sort()
    res = []
    
    n = len(arr)
    
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        left, right = i+1 , n-1
        while left < right:
            threeSum = arr[i] + arr[left] + arr[right]
            
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                
                
                # avoid duplication
                while arr[left] == arr[left - 1] and left < right:
                    left += 1
                
                while arr[right] == arr[right + 1] and left < right:
                    right -= 1
                    
    return res

# print(optimal_3sum())

    
    
def threeSum(nums): #  - - - another better way of understanding optimal approach  
    res = []
    n = len(nums)
    nums.sort()
    
    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue  # skip duplicate first element

        left, right = i + 1, n - 1
        while left < right:
            threeSum = a + nums[left] + nums[right]
            if threeSum > 0:
                right -= 1
            elif threeSum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1
                # skip duplicates on both sides
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

    return res

# print(threeSum([-1,0,1,2,-1,-4]))



# 4 sums problem - - - - Brute-force approach
def sum_4():
    
    arr = [1,0,-1,0,-2,2]
    
    n = len(arr)
    res = []
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if arr[i] + arr[j] + arr[k] + arr[l] == 0:
                        quartlet = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                        res.append(quartlet)
                        
    return res

# print(sum_4())


# 4 sum better approach
def better_4():

    arr = [1,0,-1,0,-2,2]
    arr.sort()
    n = len(arr)
    target = 0
    res = set()
    
    for i in range(n):
        for j in range(i+1, n):
            
            hash_set = set()
            for k in range(j+1, n):
                sums = arr[i] + arr[j] + arr[k]
                fourth = target - sums
                
                if fourth in hash_set:
                    temp = tuple(sorted([arr[i], arr[j], arr[k], fourth]))  
                    res.add(temp)
                hash_set.add(arr[k])    
                    
    return res

# print(better_4())


             
             
# optimal approach of 4 sum 
def optimal_4():
    
    arr = [1,0,-1,0,-2,2]
    arr.sort()
    res = []
    n = len(arr)
    target = 0
    
    # first pointer
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        
        # second pointer
        for j in range(i+1, n):
               if j > i + 1 and arr[j] == arr[j-1]:
                  continue
        
               left , right = j+1, n - 1   
               
               while left < right:
                   total = arr[i] + arr[j] + arr[left] + arr[right]
               
                
                   if total == target:
                      res.append([arr[i] , arr[j], arr[left], arr[right]])
                      
                      while left < right and arr[left] == arr[left+1]:
                          left += 1
                          
                      while left < right and arr[right] == arr[right-1]:
                          right -= 1
                          
                      left += 1
                      right -= 1
                      
                   elif total < target:
                       left += 1
                   elif total > target:
                       right -= 1    
                       
                       
    return res
                 
                 
# print(optimal_4())
                
                
                
# largest sub-array with sum 0
def sum_zero():
    
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    current_max = 0 
    max_len = 0
    prefix_sum = {}
    
    for i in arr:
        current_max += arr[i]
        
        if current_max == 0:
            max_len = max(max_len, i+1)
            
        if current_max in prefix_sum:
            max_len = max(max_len, i - prefix_sum[current_max])
        else:
            prefix_sum[current_max] = i
            
    return max_len
        

# print(sum_zero())



# count no. of subarray with given xor K
def xor():
    
    arr = [4, 2, 2, 6, 4]
    k = 6
    xor_val = 0
    hash_map = {0:1}
    cnt = 0
    
    for i in range(len(arr)):
        xor_val ^= i
        x = xor_val ^ k
        
        if x in hash_map:
           cnt += hash_map[x]
    
        if xor_val in hash_map:
            hash_map[xor_val] += 1
        else:
            hash_map[xor_val] = 1
    
        
    return cnt


# print(xor())




# merge overlapping intervals of array
# optimal approach - - - - using pointers of left and right
# if the interval is more than any subarrays we must extend the range and add it inside
def overlap():
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    intervals.sort(key=lambda x: x[0])
    merged = []
    left = intervals[0] 
    
    for right in intervals[1:]:
        if right[0] <= left[1]:
            left[1] = max(left[1], right[1])
        else:
            merged.append(left)
            left = right
            
    merged.append(left)
    return merged

# print(overlap())
            
        
        
# merge sorted array
def merge_aray():   # - - - - - my way of solving [mix of naive and better]
    
    nums1 = [1, 5, 9, 10, 15, 20]
    nums2 = [2, 3, 8, 13]
    
    i = 0
    j = 0
    
    merge = []
    
    while i < len(nums1) and j < len(nums2):
        
        if nums1[i] <= nums2[j]:
            merge.append(nums1[i])
            i += 1     
        else:
            merge.append(nums2[j])
            j += 1
            
    merge.extend(nums1[i:])
    merge.extend(nums2[j:])
    
    return merge

# print(merge_aray())    

                
                
# merge sorted array - - - - optimal approach

def optimal_merge():
    
    nums1 = [1, 5, 9, 10, 15, 20] + [0] * 4
    nums2 = [2, 3, 8, 13]
    m = 6
    n = len(nums2)
    i = m-1
    j = n-1
    k = m+n-1
    
    while i >= 0 and j >= 0:
        
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
            
        else:
            nums1[k] = nums2[j]
            j -= 1 
        k -= 1    
            
    while j >= 0:
        nums1[k] = nums2[j]
        j-=1
        k-=1
        
    return nums1

        
# print(optimal_merge())


def target():
    
    digits = [4,3,6,2,1,2] 
    n = len(digits)
       
    for i in digits:
      for j in range(i+1, n):  
        if digits[i] == digits[j]:
            return digits[i]
        else:
            return False
            
    return digits   
       
# print(target())


# find the repeating and missing elems - - - - [hashing method]
def repeating_elem():
    
    arr  = [1,1,3]
    seen = {}
    missing = None
    repeat = None
    n = len(arr)
   
    for i in arr:
        if i in seen:
            repeat = i
        else:
            seen[i] = True
            
    for j in range(1, n+1):
        if j not in seen:
            missing = j
            break         
            
    return repeat, missing

# print(repeating_elem())    

#  - - - - - - - - - - Reapeating elems are not clear on optimal approach cus it needs math and XOr 

# ---------------------------------------------                        -------------------------------------












# count inversions - - - - [ naive / brute force appraoch ]
# using pointers 
def inversions():
    
    arr = [5,3,2,4,1]
    n = len(arr)
    cnt = 0
    
    for i in range(0, n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
               cnt += 1
               
    return cnt
     
# print(inversions())    




#  - - - - - - - -  COUNT INVERSIONS   - - - - - - - - - 

# merge-sort technique for count inversions - - - - - - - [ optimal approach ]
def merge_sort(arr, temp, left, right):
    
    inv_count = 0
    if left <= right:
        mid = (left + right) // 2
        
        inv_count += merge_sort(arr, temp, left, mid)
        inv_count += merge_sort(arr, temp, mid + 1, right)
        inv_count += merge_sort(arr, temp, left, mid, right)
        
    return inv_count
    
# print(merge_sort())
    
# merge sort of the array
def merge(arr, temp, left, mid, right):
        
    i = left
    j = mid + 1
    k = left
    inv_count = 0
    
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
           temp[k] = arr[i]
           inv_count += 1
            
        else:
            
           temp[k] == arr[i]
           inv_count += (mid - i + 1)
           j += 1
        k += 1 
        
        
    # copy the remaining elems
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
        
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
        
    for i in range(left, right + 1):
        arr[i] = temp[i]
        
    return inv_count


# print(merge())







# reverse pairs  - - - - - Brute force approach
def reverse_pairs():
    
    nums = [1,3,2,3,1]
    cnt = 0
    n = len(nums)

    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] > 2 * nums[j]:
                cnt += 1

    return cnt 

# print(reverse_pairs())



# reverse pairs - - - - - - optimal one 
nums = [1,3,2,3,1]
n = len(nums)
def reverse_pairs_optimal(nums):
  
  def merge_sort(left, right):  
        
        if left >= right:
            return 0
        
        mid = (left + right) // 2 
        count = merge_sort(left, mid) + merge_sort(mid + 1, right)
        
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] >= 2 * nums[j]:
                j+=1
            count += (j-(mid + 1))
        
        # merge sort    
        temp = []
        i,j = left, mid + 1
        
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
            else:
                temp.append(nums[j])
                j += 1
            
        while i <= mid:
            temp.append(nums[i])
            i += 1
        
        while j <= right:
            temp.append(nums[j])
            j += 1
            
            
# print(reverse_pairs_optimal(nums))
        
def max_prod_subarray():
    
    arr = [2,3,-2,4]
    n = len(arr)
    max_prod = arr[0]
    
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod = prod * arr[j]
            if prod > max_prod:
                max_prod = prod
                
    return max_prod

# print(max_prod_subarray())


#  - - - - - optimized sol of maximum product subarray
#  - -  - considering 
# left = suffix and right = prefix
def optimized():
    arr = [2,3,-2,4]
    n = len(arr)
    left = 1
    right = 1
    res = arr[0]
    
    
    for i in range(n):

        if left == 0:
            left = 1
        
        if right == 0:
            right = 1
        
        left *= arr[i]
        right *= arr[n-1-i]
        
        res = max(res, left, right)
        
    return res


# print(optimized())

