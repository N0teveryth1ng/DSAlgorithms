arr = [1,2,3,4]

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
        
print(t_small)
        

