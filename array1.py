# global array
arr = [1,2,3,5,6,7,8,4]


# Largest element in a array - - - - - - - - - >
def largest_elem(arr):
    n = len(arr)
    large = arr[0]
    
    for i in range(n):
        if arr[i] > large:
            large = arr[i]
    print(large) 
    
# largest_elem(arr)            


# second largest element withut sorting
def sec_largest_elem(arr):
    n = len(arr)
    large = arr[n-1]
    
    for i in range(n):
        if arr[i] > large:
            large = arr[i]
    print(large) 
    
sec_largest_elem(arr)   

