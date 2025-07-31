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



# second largets element of an array     
def secs():
  
   arr = [3,4,5,3,4,5,8,9]
   
   largest = arr[0]
   slargest = -1 
   
   for i in arr:
       if i > largest:
           slargest = largest
           largest = i
       elif i > slargest and i < largest:
           slargest = i
           
   print("seconf - ",slargest)

# secs()                

def check(arr):
   n = len(arr)
   for i in range(1,n):
       if arr[i] < arr[i-1]:
           print('not sorted')
           return False
           
   print('sorted')        
   return True   


check(arr)