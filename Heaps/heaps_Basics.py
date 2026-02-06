""" INITIALS OF HEAPS AND MEMORIES  """

# imports 
import heapq

# LC - 215  [Kth Largest Element in an Array]
def kth_largest(arr, k):
    
    min_heap = []
    for i in arr:
        heapq.heappush(min_heap, i)
        if len(min_heap) > k:
           heapq.heappop(min_heap)
    return min_heap[0]

# print(kth_largest([1, 1, 1, 1, 2], 2))


# Kth smallest element in array
def kth_smallest(arr, k):
    
    max_heap = []
    for i in arr:
        heapq.heappush(max_heap, -i)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    return -max_heap[0]

# print(kth_smallest([1, 1, 1, 1, 2], 3))   



# min heap
def min_heap():
    nums = [5, 3, 8, 1, 2, 7]
    heapq.heapify(nums)
    return nums

# print(min_heap())


# max heap
def max_heap():
    nums = [5, 3, 8, 1, 2, 7, 9]
    max_len = [-i for i in nums]
    heapq.heapify(max_len)
    return -max_heap[0]

# print(max_heap())



# check if an array represents a min-heap or not 
def check_min_heap(arr):
    n = len(arr)
    
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] > arr[left]:
            return False
        
        if right < n and arr[i] > arr[right]:
            return False
        
    return True

# print(check_min_heap([1, 3, 5, 7, 9]))
        


# sort k sorted arrays
def sort_k_arr(arr):
    
    n = len(arr)
    heap = []
    res = []
    
    for i in range(n):
        if arr[i]:
            heapq.heappush(heap, (arr[i][0], i,0))
            
    while heap:
        val, i, pos = heapq.heappop(heap)
        res.append(val)
        
        if pos + 1 < len(arr[i]):
            next_val = arr[i][pos + 1]
            heapq.heappush(heap, (next_val, i, pos + 1))
            
    return res    
    
# print(sort_k_arr([[1,4,7], [2,5,8], [3,6,9]]))
    
    
    
# merge k sorted lists - [lc - 23] 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 
        
        
    def merge_K_list(self, lists):
        if not lists:
            return None
        
        while len(lists) > 1:
            mergedList = []
            
            for i in range(0, len(lists), 2):
               l1 = lists[i]  
               l2 = lists[i + 1] if (i+1) < len(lists) else None
               mergedList.append(self.mergeList(l1, l2))
            lists = mergedList
        return lists[0] 


    def mergeList(self, l1, l2):
        
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
        
        curr.next = l1 if l1 else l2 
        return dummy.next 
    
    
    
# heap sort  
def heap_sort(arr):
    
    heapq.heapify(arr)
    n = len(arr)
    res = [0] * n
    
    for i in range(n):
        min = heapq.heappop(arr)
        res.append(min[i])
        
    return res

# print(heap_sort([40, 10, 20, 30, 10, 20]))


# sort based on their corresponding ranks 
def ranking_corres(arr):
    
    heap = [(val, i) for i, val in enumerate(arr)]
    heapq.heapify(heap)
    
    rank = 1
    current = 1
    prev = None
    res = [0] * len(arr)
    
    while heap:
        val, idx = heapq.heappop(heap)
        
        if current != prev:
            current = rank
            rank += 1
            prev = val
            
        res[idx] = current
        
    return res
      
# print(ranking_corres([100,100,100]))




# ranking based on medal system 
def lc_506(arr):
    
    heap = [(val, i) for i, val in enumerate(arr)]
    heapq.heapify(heap)
    
    rank = 1
    res = [""] * len(arr)
    
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

# print(lc_506([5,4,3,2,1]))


# rank transform array [lc - 1331]
def arrayRankTransform(arr):
        heap = [(val, i) for i, val in enumerate(arr)]
        heapq.heapify(heap)

        res = [0] * len(arr)
        rank = 1
        prev = None
        current = 1

        while heap:
            val, idx = heapq.heappop(heap)
    
            while current != prev:
                current = rank
                rank += 1
                prev = val

            res[idx] = current

        return res 
    
# print(arrayRankTransform([100,100,100]))


# lc - 621
from collections import Counter
def task_scheduler(tasks, n):
    
    freq = Counter(tasks)
    
    maxFreq = max(freq.values())
    maxCount = sum(1 for v in freq.values() if v == maxFreq)
    
    forced_time = (maxFreq - 1) * (n + 1) + maxCount
    
    return max(len(tasks), forced_time)




# hand of straights - [lc - 846]
def hands_straight(hand, k):
    heap = [i for i in range(hand)]
    heapq.heapify(heap)
    
    if len(hand) % k == 0:
        return True
    
    freq = Counter(hand)
    minfreq = min(freq.values())
    
    while heap:
        if len(hand) % k != 0:
            return False
        
    return True


# print(hands_straight([1,2,3,6,2,3,4,7,8]))