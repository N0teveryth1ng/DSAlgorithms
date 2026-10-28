arr = [0,0,1,2,3,4]

def t_smallest():
    small = float("inf")
    s_small = float("inf")
    t_small = float("inf")
    
    n = len(arr)
    for i in range(0, n):
        if arr[i] < small:
            t_small = s_small
            s_small = small
            small = arr[i]
            
        # if its the new second smallest 
        elif arr[i] < s_small and arr[i] != small:
            t_small = s_small
            s_small = arr[i]
            
        # if it should be the new third smallest
        elif arr[i] < t_small and arr[i] != s_small and arr[i] != small:
            t_small = arr[i]
        
# print(t_smallest())
        




# : Move all zeros to the end of an array, keeping the order of other elements unchanged.

def move_end():
    insert_pos = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1
            
    return arr
         
# print(move_end())   

        
        
        
# remove duplics
def remove():
    
    if not arr:
        return arr
    
    i = 0
    for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
                
    return arr[:i+1]

# print(remove())
            
            
            
            
            
            
            
            
            

            
def move_zeroes():
    
    insert_pos = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1
            
    return arr



def rmve_duplicate():
    
    i = 0
    for j in range(1, len(arr)):
        if arr[i] == arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            arr[i] = arr[j]
            
    return arr[:i+1]
            
        
        
        
        
        
def move_it():
    
    insert_pos = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[insert_pos] = arr[insert_pos], arr[i]
            insert_pos += 1
            
    return arr
# print(move_it())




def remove_copy():
    
    i = 0
    
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1
            arr[i] = arr[j]
            
    return arr[:i+1]

# print(remove_copy())




# linear search
def linear_search(arrr, target):
    
    for i in range(len(arrr)):
        if arrr[i] == target:
            return i
        
    return -1

# print(linear_search([1, 2, 2, 3, 2, 4, 1], 4))


# check sorted
def check_sorted(arr):

    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]: 
            return False
            
    return True

# print(check_sorted([1, 4, 3, 1, 5]))


# find missing nums
def find_miss(nums, n):
    
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    result = expected_sum - actual_sum    
        
    return result


 
#  2 sum
def two_sum(nums, tagret):
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == tagret:
                return [i, j]
            
    return -1

# print(two_sum([1, 2, 4, 5], 9))



# 2 sum - optimized hashmap. 
def two_sum_optimised(nums, target):
    
    temp = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        if diff in temp:
            return [temp[diff], i]
        else:
            temp[n] = i
    return

# print(two_sum_optimised([1, 2, 4, 5], 9))



    
# lC  - 217
def duplics(nums):
    
    seen = set()
    
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
        
    return False



# only appears once - lc - 136
# (brute force approach)
def appears(nums):
    
    count = {}
    
    # dump all in dict first
    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
   
    # then extarct
    for i in nums:            
        if count[i] == 1:
            return nums[i]
        
    return False
        
     
    
    
    
    
# valid anagram lc - 242
# brute force
def valid_anagram(s,t):
    
    temp = {}
    temp2 = {}
    
    # ith one
    for i in s:
        if i in temp:
           temp[i] += 1
        else:
            temp[i] = 1
            
    # jth one
    for j in t:
        if j in temp2:
            temp2[j] += 1
        else:
            temp2[j] = 1
            
    # run check 
    if temp == temp2:
        return True
    
    return False
              
    
# optimised version
def valid_anagram_optimised(s,t):
    
    # run check
    if len(i) != len(j):
        return False
    
    count = {}
    
    # ith one 
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    # jth one 
    for j in t:
        if j in count:
            count[j] -= 1
            if count[j] < 0:  # <-- edge case if less than 0
                return False
        else:
            return False
            
    return True


# leetcode- 49
def grouping(str):
    
    count = {}
    
    # run a check
    for word in str:
        
        # sorted by default
        key = "".join(sorted(word))
        
        # If key not in count, create an empty key. 
        if key not in count:
            count[key] = []
            
        # and add to the empty key
        count[key].append(word)     
        
    return list(count.values())













# 2 sum
def test(nums, target):
    
    count = {}
    
    for i, n in enumerate(nums):
        diff = target - n
        
        if diff in count:
            return [count[diff], i]
        
        count[n] = i
    return False
            
    
    
    
    
# duplics
def find_duplics(nums):
    
    seen = set()     
    
    for i in nums:
        if i in seen:
            return True
        
        seen.add(i)
    return False



# lc - 125
def valid_palindrome(str):
    
    i = 0
    j = len(str) - 1

    while i < j:
        
        if not str[i].isalnum():
            i += 1
        elif not str[j].isalnum():
            j -= 1
        elif str[i].lower() != str[j].lower():
            return False
        else:
            i += 1
            j -= 1
        
    return True  




# 2 sum - II
def test(target, nums):
    
    count = {}
    
    for i,n in enumerate(len(nums)):
        diff = target - n
        if diff in count:
            return [count[diff], i]
        
        count[n] = i
        
    
# lc - 167
def two_sum_II(target, nums):
    
    i = 0
    j = len(nums) - 1
    
    while i < j:
        sums = nums[i] + nums[j]
   
        if sums == target:
            return [i + 1, j + 1]
        elif sums < target:
            i += 1
        elif sums > target:
            j -= 1
            
    return []



# lc - 15
def three_sum(nums, target):
    
    nums.sort()
    res = []
    
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        j = i + 1
        k = len(nums) - 1
        
        while j < k:
            total = nums[i] + nums[j] + nums[k]
           
            if total == target:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
            elif total < target:
                j += 1
            else:
                k -= 1
            
    return res




# 