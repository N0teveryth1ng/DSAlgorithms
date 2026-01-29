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

print(kth_smallest([1, 1, 1, 1, 2], 3))



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
        
        


# 