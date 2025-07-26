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
arr = [1,2,3,4,5]
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr        
                
print(bubble_sort(arr))


# 