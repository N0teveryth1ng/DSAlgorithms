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
    
    # handling edgecases
    if len(hand) % k != 0:
        return False
    
    # hashmap
    count = {}
    for i in hand:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    minheap = list(count.keys())
    heapq.heapify(minheap)
    
    
    while minheap:
        start = minheap[0]
        
        for i in range(start, start + k):
            if i not in count:
                return False
            count[i] -= 1
            if count[i] == 0:
                if i != minheap[0]:
                    return False
                heapq.heappop(minheap)
                    
    return True

# print(hands_straight([1,2,3,4,5], 4))










""" HARD PROBLEMS OF HEAPS """

# design twitter/X - [lc - 355] 
class Twitter:
    def __init__(self):
        self.time = 0  
        self.tweets = {}  
        self.following = {}
    
    def posttweet(self, userID, tweetID):
        if userID not in self.tweets:
            self.tweets[userID] = []
        self.time += 1
        self.tweets[userID].append((self.time, tweetID))
        
    def follow(self, followerID, followeeID):
        if followerID not in self.following:
            self.following[followerID] = set()
        self.following[followerID].add(followeeID)
        
        
    def unfollow(self, followerID, followeeID):
        if followerID in self.following and followeeID in self.following[followerID]:
            self.following[followerID].remove(followeeID)
        
        
    def getfeeds(self, userID):
        people = self.following.get(userID, set()).copy()
        people.add(userID)
        
        all_tweets = []
        for person in people:
            if person in self.tweets:
                all_tweets.extend(self.tweets[person])
            
        all_tweets.sort(reverse=True)
        return [tweetId for (self.time, tweetId) in all_tweets[:10]]    
        
        
     
# twitter = Twitter()
# twitter.posttweet(1, 5)      
# twitter.posttweet(1, 3)      
# twitter.follow(2, 1)        
# twitter.follow(1, 2)        
# twitter.getfeeds(1)

# print("get feeds -", twitter.getfeeds(1))




# minimum costs to connect two sticks 
def connect_sticks(arr):
    
    if len(arr) <= 1:
        return 0
    
    heap = arr[:]
    heapq.heapify(heap)
    
    total = 0
        
    while len(heap) > 1:
        # pop two elems
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        
        # connect them
        cost = first + second
        
        # update total
        total += cost 

        # push new sticks
        heapq.heappush(heap, cost)
        
    return total 

# print(connect_sticks([2,3,4]))



# Kth Largest Element in a Stream -- [lc - 703]
def Kth_largest(arr, k):
    
    heap = []
    for i in arr:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0] if heap else None

# print(kth_largest([3, 2, 1, 5, 6, 4], 2))



# find median from steam of data    
class medianFinder:
    def __init__(self):
        self.small = []
        self.large = []
        
    def addNum(self, num):
        # add to appropriate heaps
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
            
            
        # balance the heaps 
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)       
        else:
            val =  heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
     
     
     
    #  find median fucntion 
    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
    
    
    
    
    
# k - frequent elems - [lc - 347]
def k_freqs(arr, k):
    
    count = Counter(arr)
    
    heap = []
    for i,val in count.items():
        heapq.heappush(heap, (val, i))
        if len(heap) > k:
            heapq.heappop(heap)
    return [i for neg_val, i in heap]

# print(k_freqs([1,2,1,2,1,2,3,1,3,2], 2))




