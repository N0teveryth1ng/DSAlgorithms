arr = [0,0,1,2,3,4]

def t_smallest():
    small = float("inf")
    s_small = float("inf")
    t_small = float("inf")
    
    n = len(arr)
    for i in range(0, n):
        if arr[i] < small:
            t_small = s_small
            s_small = small
            small = arr[i]
            
        # if its the new second smallest 
        elif arr[i] < s_small and arr[i] != small:
            t_small = s_small
            s_small = arr[i]
            
        # if it should be the new third smallest
        elif arr[i] < t_small and arr[i] != s_small and arr[i] != small:
            t_small = arr[i]
        
# print(t_smallest())
        




# : Move all zeros to the end of an array, keeping the order of other elements unchanged.

def move_end():
    insert_pos = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[insert_pos], arr[i] = arr[i], arr[insert_pos]
            insert_pos += 1
            
    return arr
         
# print(move_end())   

        
        
        
# remove duplics
def remove():
    
    if not arr:
        return arr
    
    i = 0
    for j in range(1, len(arr)):
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
                
    return arr[:i+1]

# print(remove())
            
            
            
            
