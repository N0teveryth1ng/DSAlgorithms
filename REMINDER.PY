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




# DATES - [30/01/2026]
# q1 - min_heap and max_heap
# q2 - check if min_heap exists or not
# q3 - kth largest elem

import heapq

# q3 - Kth largest 
def q3(arr, k):
    heap = []
    
    for i in arr:
        heapq.heappush(heap, i)
        if len(heap) > k:
           heapq.heappop(heap)
    return heap[0]

# print(q3([1, 1, 1, 1, 2], 2))

# q1 - min heap
def q1_minHeap(arr):

    heapq.heapify(arr)
    return arr

# print(q1_minHeap([1, 3, 9, 1, 2]))
        
# q1 - max heap
def q1_maxHeap(arr):
    maxlen = [-i for i in arr]
    heapq.heapify(maxlen)
    return -maxlen[0]
    
# print(q1_maxHeap([1, 1, 9, 1, 2]))


# q2 - check if min heap exists or not 
def q2(arr):
    
    n = len(arr)
    
    for i in range(n):
        
        left = 2 * i + 1
        right = 2 * i + 2
        
        while left < n and arr[left] < arr[i]:
            return False
        
        while right < n and arr[right] < arr[i]:
            return False
        
    return True

# print(q2([9, 1, 1, 1, 2]))




# 
def test(arr, k):
    
    n = len(arr)
    maps = {}
    left = 0
    maxlen = 0
    
    for right in range(n):
        if arr[right] in maps:
            maps[arr[right]] += 1
        else:
            maps[arr[right]] = 1
            
            
        while len(maps) > k:
            maps[arr[left]] -= 1
            if maps[arr[left]] == 0:
                del maps[arr[left]]
            left += 1
        
        maxlen = max(maxlen, right-left+1)
            
    return maxlen





# merge K sorted lists  [lc - 23]
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
        
    def mergeLists(self, lists):
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(self.merge(l1, l2))  
            lists = mergedList
        return lists[0]
    
    
    def merge(self, l1, l2):
        dummy = ListNode()
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next 
            else:
                curr.next = l2
                l2 = l2.next 
            curr = curr.next
            
        curr = l1 if l1 else l2
        return dummy.next            
    
    
    
    
# rank corresponding in place without sorting       
def test(arr):
    heap = [(val, i) for i, val in enumerate(arr)]
    res = [0] *len(arr)
    heapq.heapify(heap)
    
    prev = None
    current = 1
    rank = 1
    
    while heap:
        val, idx = heapq.heappop(heap)
        
        if current != prev:
            current = rank
            rank += 1
            prev = val
            
        res[idx] = current
        
    return res

# print(test([40, 10, 20, 30, 10, 20]))




# date - 6th feb, 2026
# lc - 506
def test(arr):
    
    heap = [(val, i) for i, val in enumerate(arr)]
    heapq.heapify(heap)
    
    res = [""] * len(arr)
    rank = 1
    
    while heap:
        val, idx = heapq.heappop(heap)
        
        if rank == 1:
            res[idx] = "gold medal"
        elif rank == 2:
            res[idx] = "silver medal"
        elif rank == 3:
            res[idx] = "bronze medal"
        else:
            res[idx] = str(rank)
            
        rank += 1
        
    return sorted(res)

# print(test([5,4,3,2,1]))  
    
    
    
def hand_straight(hands, k):
    
    if len(hands) % k != 0:
        return False
    
    maps = {}
    for i in hands:
        if i in maps:
            maps[i] += 1
        else:
            maps[i] = 1
    
    minheap = list(maps.values())        
    heapq.heapify(minheap)
    
    
    while maps:
        start = minheap[0]
        
        for i in range(start, start + k):
            if i not in maps:
                return False
            maps[i] -= 1
            if maps[i] == 0:
                if i != maps[i]:
                    return False
                heapq.heappop(minheap)
    
    return True

# print(hand_straight([1,2,3,4,5], 4))





