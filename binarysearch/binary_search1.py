#  - - - - - - This file is for binary search process and its working models for more better understading of how things work in all 
# - - - - - - - all sort of arrays

#  - - - - - - brute force of Binary search
def test():
    
    nums =   [-1,0,3,5,9,12]
    target = 9
    n = len(nums)
    
    for i in len(nums):
        if target == nums[i]:
            return i
    return -1    
        
# print(test())

#   - - - - - - - Binary search - - - optimal way 
def binary():
    
    nums = [-1,0,3,5,9,12]
    target = 9
    n = len(nums)
    
    low, high = 0, n-1
    mid = (low + high) // 2
    
    while low <= high:
        
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

# print(binary())



# binary search - - - - most optimal approach using recursion
def binary_recursive(arr, target, left, right):
    
    if left > right:
        return -1
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_recursive(arr, target, left, mid - 1)
    else:
        return binary_recursive(arr, target, mid + 1, right)
    

def test():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    return binary_recursive(nums, target, 0, len(nums)-1)

# print(test())   
  
  
  
#  - - - - - - - - - - - - FLOOR AND CEILING  - - - - - - - - - - - - - 
# search insert position - - - - - - - - simple approach to solve the problem
def search_pos():
    
    arr = [1,3,5,6]
    target = 5
    
    n = len(arr)
    low, high = 0, n-1
    res = n
    
    while low <= high:

        mid = ( low + high ) // 2
        
        if arr[mid] == target:
            return mid

        if arr[mid] >= n:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return res

# print(search_pos())
    
    
    
# upper bound
def upper_bnd():
    
    arr = [1,3,5,5,6]    
    n = len(arr)
    low, high = 0, n-1
    res = n
    
    while low <= high:

        mid = ( low + high ) // 2
        
        if arr[mid] > n:
            res = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return res


# print(upper_bnd())


#  - - - - - - - - First and last position of an element in a sorted array - - - - - - - - - - 
#  - Approach ->  considering an low and high bound acts as 2 pointers to find the first and last elems

def first_last_bound():
    
    nums = [5,7,7,8,8,10]
    target = 8
    n = len(nums)
    
    first = -1
    low, high = 0, n-1
    
    # lower bound
    while low <= high:
        mid  = (low + high) // 2
        
        if nums[mid] == target:
            first = mid
            high = mid - 1
        
        elif nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
            
            
    # upper bound
    last = -1
    low, high = 0, n-1 
     
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            last = mid
            low = mid + 1
        
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
            
    return first, last

# print(first_last_bound())


# optimal approach  - - first and last position of the array
class solution(object):
    def binary_search(self, arr, target, leftBias):
        
        arr = [5,7,7,8,8,10]
        target = 8
        n = len(arr)
        left , right = 0, n-1
        res = -1
    
        while left <= right:
            mid = (left + right) // 2
            
            if target > arr[mid]:
                left = mid + 1
                
            elif target < arr[mid]:
                right = mid - 1
            
            else:
                res = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        return res
                           
           
    def firstLastBound(self, arr, target):
        left = self.binary_search(arr, target, True)
        right = self.binary_search(arr, target, False)
        return [left, right]
    
    


# search in rotated sorted array 
def rotated():
    
    arr = [4,5,6,7,0,1,2]
    target = 0    
    
    n = len(arr)
    low, high = 0, n-1
    i = -1
    
    
    # left sorted part
    while low <= high:
        mid = (low + high) // 2
         
        # found target
        if arr[mid] == target:
            return mid 
         
         
        # lower bound
        if arr[low] <= arr[mid]:
           if arr[low] <= target and target <= arr[mid]:
               high = mid - 1
           else:
               low = mid + 1
        
        # upper bound
        else:
           if arr[low] >= target and target >= arr[mid]:
               low = mid + 1
           else:   
               high = mid - 1
                 
             
    return i

# print(rotated())   





# search rotated array - 2
 
def rotated_2():
    
    arr = [2,5,6,0,0,1,2]
    target = 0
    n = len(arr)
    low , high = 0, n-1
   

    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low = low + 1
            high = high - 1 
            continue
        
        if arr[low] <= arr[mid]:
            if arr[low] <= target and target <= arr[mid] :
                high = mid - 1
            else:
                low = mid + 1
                
        else:
            if arr[mid] <= target and target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
                
    return False 
            
            
# print(rotated_2())
        
        
        
        
# find minimum in rotated sorted arrray - - - - - ( return the lowest int in the array)
def sorted_arr():
    
    arr = [3,4,5,1,2]
    n = len(arr)
    
    low, high = 0, n-1
    ans = float("inf")
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[low] <= arr[high]: #- - - - - this is not needed. but this can minutely improves time complexity  
            ans = min(ans, arr[low])
            break
        
        # checks for bounds
        if arr[low] <= arr[mid]: 
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            high = mid - 1
            ans = min(ans, arr[mid])
      
    return ans

# print(sorted_arr())



# sigle element in the sorted array 
#   - - - - - - brute force method 
def single_elem():
    
    arr = [1,1,2,3,3,4,4,8,8]
    n = len(arr)
    
    for i in range(n):
        
        if i == 0:    
            if arr[i] != arr[i+1]:
               return arr[i]
        elif i == n-1:
            if arr[i] != arr[i-1]:
               return arr[i]
        else:
            if arr[i] != arr[i+1] and arr[i] != arr[i-1]:
                return arr[i]  
          
        
    return False
    
# print(single_elem())    
    

#  - - - - - - -     optimal approach of single element 
def optimal_elem():
    
     nums = [1,1,2,3,3,4,4,8,8]
     n = len(nums)
     
     low, high = 1, n-2
     
     while low <= high:
         
        mid = (low + high) // 2

        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]
        
        if mid % 2 == 1 and nums[mid] == nums[mid - 1] and mid % 2 == 0 and nums[mid] == nums[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
            
            
     return -1
 
 
# print(optimal_elem())
            
            
             
#  - - - - - - find the peak element 
#  - - - - - linear search implemented solution 
def peak():
    
    arr = [1,2,3,1]
    n = len(arr)
    
    low, high = 0 , n-1
    
    while low <= high:
        mid = (low + high) // 2
        
        # check for left and right up hill iteration 
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1
            
        return low 
     

# print(peak()) 
            
            
def optimal_peak():
    
    arr = [1,2,3,1]
    n = len(arr)
    
    low, high = 0 , n-1
    
    while low <= high:
        mid = (low + high) // 2
        
        left_val = arr[mid-1] if mid > 0 else float('-inf')
        right_val = arr[mid+1] if mid < n-1 else float('-inf')
            
        
        # direct check for the first elem id peak
        if arr[mid] > left_val and arr[mid] > right_val:
            return mid
        
        elif arr[mid] > arr[mid-1]:
            low = mid + 1
        
        elif arr[mid] > arr[mid+1]:
            high = mid - 1
    
    return -1


# print(optimal_peak())

# optimal shortest peak finding  - - - - 
def test():
    
    nums = [1,2,3,1]     
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l
        
        
# print(test())



# 
        