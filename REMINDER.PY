""" HERE U WILL SOLVE DAILY REVISION GIVEN BY THE SYSTEM AND ACTIVELY RECALL THE PATTERNS """

"""
each Q's --> 15 mins

"""

# DATED = [29/01/2026]
# q1 - lc - 15 (3 sum) 
# q2 - lc - 167 (2 sum II)

def q1(nums): # - - - 3sum 
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n-2):
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i+1
        right = n-1
        
        while left < right:
            current = nums[i] + nums[left] + nums[right]
            
            if current > 0:
                right -= 1
            elif current < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                
        # avoid dupicates 
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
            
    return res 
            
# print(q1([-1,0,1,2,-1,-4]))



def q2(nums, target):  # - - - 2sum - II
    
    n = len(nums)
    
    left = 0
    right = n-1
    
    while left < right:
        current = nums[left] + nums[right]
        
        if current == target:
            return [left + 1, right + 1]
        elif current > target:
            right -= 1
        else:
            left += 1
        
    return []
            
# print(q2([2,7,11,15], 9))




