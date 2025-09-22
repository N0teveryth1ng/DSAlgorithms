# Binary search on 2d arrays


#  - - - - - brute force to row with max nums of 1's
#  time complexity of M x N (m * n) 
def row_max():
    
    matrix = [
    [0, 0, 1, 1],   # row 0
    [0, 1, 1, 1],   # row 1
    [0, 0, 0, 1]    # row 2
    ]

    rows, cols = len(matrix), len(matrix[0])
    max_cnt = 0
    max_row = -1
    
    
    for i in range(rows):
        count = 0
        
        for j in range(cols):
            if matrix[i][j] == 1:
                count += 1 
                
        if count > max_cnt:
            max_cnt = count
            max_row = i
            
    return max_row

# print(row_max())
  
  
#  - - - - - optimal approach 

def optimal_row():
    
    matrix = [
    [0, 0, 1, 1],   # row 0
    [0, 1, 1, 1],   # row 1
    [0, 0, 0, 1]    # row 2
    ]
            
    # searching for 1's in array
    n = len(matrix)
    max_row = -1
    max_idx = 0
    cols = len(matrix[0])
    
    # searching for 1's in the rows 
    for i in range(n):
        low, high = 0, cols - 1
        first_idx = cols
        
        while low <= high:
            mid = (low + high) // 2
            
            if matrix[i][mid] == 1:
                first_idx = mid
                high = mid - 1
            else:
                low = mid + 1
                
                
        # comparing prev nums
        count = cols - first_idx
        if count > max_idx:
            max_idx = count
            max_row = i
            
    return max_row

# print(optimal_row())
    
    
#  - - - - - - - search target a 2d matrix 
def search_target():
    
      matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
      target = 9
    
      rows = len(matrix)
      cols = len(matrix[0])
      
      # search in the matrix  
      for i in range(rows):
          
          low, high = 0, cols - 1
          
          while low <= high:
              mid = (low + high) // 2
              
              if matrix[i][mid] == target:
                   return True
              
              elif target < matrix[i][mid]: 
                   high = mid - 1
              else:
                   low = mid + 1
                   
                   
      return False
   
# print(search_target())
                    
              
# - - - - optimal approach - - - 
# even if this is a optimal one it is still hve the same time complexity

def optimal():
    
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 30
      
    n = len(matrix)
    row, col = 0, n-1  
     
     
    while row <= n and col >= 0:
        
        if matrix[row][col] == target:
            return [row, col] 
        
        elif target < matrix[row][col]:
            col -= 1
        else:
            row += 1
            
    return [-1, -1] 

# print(optimal())   



#  - - find the peak element 2  - - -  matrix calculation [ 3 x 3 ]
def peak_elem():
    
    mat = [[1,4],[3,2]]
    
    n,m = len(mat), len(mat[0])
    low, high = 0, m-1
    
    while low <= high:
        mid = (low + high) // 2
        
        max_row = 0
        
        for i in range(n):
            if mat[i][mid] > mat[max_row][mid]:
               max_row = i
        
        left = mat[max_row][mid - 1] if mid - 1 >= 0 else -1  
        right = mat[max_row][mid + 1] if mid + 1 <= m else -1 
        
        if mat[max_row][mid] > left and mat[max_row][mid] > right:
            return [max_row, mid]
        elif mat[max_row][mid] > right:    
            high = mid - 1
        else:
            low = mid + 1
   
            
    return -1

# print(peak_elem())    




                    





                   
                   
                   
                   
    
