# global array
# arr = [1,2,3,5,6,7,8,4]
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

# length = check_dups(arr)
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
def brute(): # - - - - - - Not mmost efficeint 
   
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


# Linear search - - - - - - - - [Easy as hell]
def linear_search():
    arr = [1,2,3,4,5,6]
    n = len(arr)
    
    for i in range(n):
        if arr[i] == 5:
            return i
            
    return arr

# print(linear_search())
    
    
# UNION FIND - - - - - - [Brute force method]
def union():
    
    arr1 = [1,2,3,3,4]
    arr2 = [3,4,5,5,6,3]
    
    sets = []
    
    for i in arr1:
      if i not in sets:    
        sets.append(i)
        
    for i in arr2:
      if i not in sets: 
        sets.append(i)
        
    return sets

# print(union())


# using 2 pointers in array - - - - - -[still unclear will see onward]

def pointer():
    
    arr1 = [1,2,3,3,4]
    arr2 = [3,4,5,5,6,3]
    
    n1 = len(arr1)
    n2 = len(arr2)
    
    i,j = 0,0
    
    union = []
    
    while i < n1 and j < n2:
        if len(union) > 0 and union[-1] == arr1[i]:
            i += 1 
            continue
        
        if len(union) > 0 and union[-1] == arr2[j]:
            j += 1
            continue
        
        
        
        
        if arr1[i] < arr2[j]:
            union.append(arr1[i])
            i += 1
            
        elif arr2[j] > arr1[i]:
            union.append(arr2[j])
            j += 1
            
        else:
            union.append(arr1[i])
            i += 1
            j += 1
            
        
    while i < n1:
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
            
    while j < n2:
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
            
    return union
    
# print(pointer())

# brute force method of mising num from 1 to N
def find_num1():
    arr = [1,2,4,5]
    n = len(arr)
    
    for i in range(n+1):
        if i not in arr:
            return i 
        
    return arr

# print(find_num1())        
        

def find_num(): # better approach method [ takes 2700 ms ]
    
    arr = [1,2,4,5]
    n = len(arr) 
    num_set = set(arr)
    
    for i in range(1, n+1):
        if i not in num_set:
            return i
            
    return arr

# print(find_num())  


def xor(arr): # - - - - - 10 ms delay
    
    n = len(arr)
    
    xor1 = 0
    for i in range(n+1):      
        xor1 = xor1 ^ i
        
    xor2 = 0
    for i in arr:
        xor2 = xor2 ^ i 
        
    return xor1 ^ xor2

arr = [1,2,4,5]
# print(xor(arr))


# find the consecutive of all
def consec():
    arr = [1,1,1,0,1,1,0,1,1,1,1]
    n = len(arr)
    maxi = 0    
    count = 0
    
    for i in range(n):
        if arr[i] == 1:
            count += 1
            maxi  = max(maxi, count)
            
        else:
            count = 0
            
    return maxi


# print(consec())
            
# every num appears twice sort the one appearance num 

def twice_appear():
    arr = [1,1,2,2,3,4,4,5,5]
    
    n = len(arr)
    cnt = {}
    
    for i in arr:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
            
    
    for i in cnt:
        if cnt[i] == 1:
            return i

# print(twice_appear())
        
    
def remove_elems():
    arr = [1,1,3,4,5,6,7,3,3]
    n = len(arr)
    val = 3
    temp = []
    for i in arr:
        if arr[i] != val:
            temp.append(i)
        
    return temp

print(remove_elems())
            