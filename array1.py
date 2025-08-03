# global array
arr = [1,2,3,5,6,7,8,4]
# arr = [3,3,4,5,6,6,8,8,9]

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
           
   print("second - ",slargest)

# secs()                

# check if an arr is sorted or not
def check(arr):
   n = len(arr)
   for i in range(1,n):
       if arr[i] < arr[i-1]:
           print('not sorted')
           return False
           
   print('sorted')        
   return True   

# check(arr)


# sort duplicated vals from the arr
def check_dups(arr):
        
    if not arr:
        return 
    
    j = 0

    for i in range(1, len(arr)):
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i] 
    
    return j + 1

length = check_dups(arr)
# print(arr[:length])

# optimal approach but takes high space [not good for DSA]
def remove(arr):
    res = []
    for i in arr:
        if i not in res:
            res.append(i)
            
    return res

# print(remove(arr))


# LEFT Rotate process by one place 

def left_rot():

  arr = [1,2,3,5,6,7,8,4]
  n = len(arr)
  temp = arr[0]
  
  for i in range(1, n):    
      arr[i-1] = arr[i]  
      
  
  arr[n-1] = temp
  return arr


# print(left_rot())


def right_rot():
     
   arr = [2,3,4,4,7,7,8]
   n = len(arr)
   temp = arr[n-1]
   
   for i in range(n-2,-1,-1):
       arr[i+1] = arr[i]
   
   arr[0] = temp
   return arr

# print(right_rot()) 
              
       
# Left rotate array by D places  - - - - -[ Right rotate is bit hard for me to understand ]
def left_d():
    
    arr = [1,2,3,4,5,6,7]
    n = len(arr)
    d = 3
    temp = []
    
    for i in range(d):
        temp.append(arr[i])
        
    for i in range(d, n):
        arr[i-d] = arr[i]
        
    for i in range(d):
        arr[n-d + i] = temp[i]
            
    print(arr)
    
# left_d()        



# last the zero nums in an arr
def non_zero(): # - - - - - - most efficient approach
    arr = [1,2,3,0,5,0,5,3,0,9,6,5]
    n = len(arr)
    pos = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
            
    for i in range(pos,n):            
       arr[i] = 0
      
    return arr
        
        
# print(non_zero())


# brute force method of sending 0s to end
def brute(): # - - - - - -Not mmost efficeint 
   
   arr = [1,2,0,3,4,0,0,5,4,0]
   n = len(arr)
   temp = []
   
   for i in range(n):
       if arr[i] != 0:
           temp.append(arr[i])
   
   for i in range(len(temp)):
       arr[i] = temp[i]
       
   for i in range(len(temp), n):
       arr[i] = 0
       
   return arr

# print(brute())