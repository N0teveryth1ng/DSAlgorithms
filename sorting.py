# Sorting

# global arr var 
# arr = [5,1,1,2,0,0]


# selection sorting of an array ------------------->
# swapping function
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    
# sorting function --- selcts the max min and swaps
def selection_sorting(arr):
    
    n = len(arr)
    for i in range(n):
        minimum = i
        for j in range(i+1, n):
            if arr[j] < arr[minimum]:
                minimum = j
        swap(arr, i, minimum)
    return arr

# print(selection_sorting(arr))
            
                      
# Bubble sort --- compares and swaps [ very slow ]
# arr = [5,4,6,3,9]
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr        
                
# print(bubble_sort(arr))


# Insertion sort with for,while - - - - - more like inplace sort [also very stupid]
# arr = [3,4,61,4,5]
def inplace(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        
        while j>=0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
            
        arr[j+1] = key        
    return arr

# print(inplace(arr))

# Insertion with nested for loop - - - - - also very stupid 
def nested():
    arr = [5,46,32,3,89]
    n = len(arr)
    
    for i in range(1,n):
        insert_index = i
        current_val = arr[i] 
        
        for j in range(i-1,-1,-1):
            if arr[j] > current_val:
                arr[j+1] = arr[j]
                insert_index = j
            
        arr[insert_index] = current_val
    return arr
        
        
# print(nested())




# < - - - - - - - Merge-Sort algo - - - - - - - >

arr = [23,5,6,7,89,35,65]

# merge the sorted arrays
def merge(arr,low,high):
    
    if low >= high:
        return 
    
    mid = (low + high) // 2
    merge(arr,low, mid)
    merge(arr, mid + 1, high)
    merge_arr(arr, low, mid, high)


# merge fucntion for merge sort 
def merge_arr(arr,low,mid,high):    
    
    temp = []
    left = low
    right = mid + 1
    
    while left <= mid and right <= high:
        
        if arr[left] <= arr[right]:
            temp.append(arr[left]) # stores temporarily
            left += 1 # continue checking
            
        else:
            temp.append(arr[right])
            right += 1 # continue checking 
            

            # if anything still gets left at left 
    while left <= mid:
            temp.append(arr[left])
            left += 1
            
            # if anything still gets left at right
    while right <= high:
            temp.append(arr[right])
            right += 1
            
            # copy array back to original array
    for i in range(len(temp)):
            arr[low+i] = temp[i]
            
                
merge(arr,0,len(arr)-1)
# print(arr)  



# quick sort - - - - - - - - >

def quick_sort(arr,left, right):
    if left < right:
        part_pos = partition(arr, left, right) 
        quick_sort(arr, left,part_pos) # sort left arr
        quick_sort(arr, part_pos + 1, right) # sort right arr

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    j = right - 1

    while i <= j:
        while i <= right and arr[i] <= pivot: 
            i += 1
            
        while i <= right and arr[j] >= pivot:
            j -= 1
            
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
        
    
    arr[i], arr[right] = arr[right], arr[i]
    return i 


quick_sort(arr,0, len(arr) - 1)
print(arr)     
    
    
    
