# Final pysg to stack and queue concepts 

# sliding window maximum 
def slding_window():
    
    arr = [1,3,-1,-3,5,3,6,7]
    k = 3
    n = len(arr)
    stack = []
    
    for i in range(n, k):
        maxi = arr[i]
        for j in range(i+1, k):
            maxi = max(maxi, arr[j])
        stack.append(maxi)
        
    return stack




        
        