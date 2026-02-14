# GREEDY PART ONE [EASY]


# assign cookies [ lc - 455]
def assign_cookies(g,s):
    
    g.sort()
    s.sort()
    
    i = j = 0
    
    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1
        
    return i 

# print(assign_cookies([1,2,3], [1,1]))




# fraction knapstack
def fraction_knapstack(items, capacity):
    
    items.sort(key=lambda x: x[0]/x[1], reverse=True)
    
    total_val = 0
    
    for val, weight in items:
        if capacity >= weight:
           total_val += val
           capacity -= weight
           
        else:
            fraction = capacity / weight
            total_val += fraction * val
            break
    
    return total_val

# print(fraction_knapstack([(60, 10), (100, 20), (120, 30)], 50))



# lemonade change - - - [lc - 860]
def lemonade_change(bills):
    
    five = ten = 0
    
    for i in bills:
        if i == 5:
            five += 1
        if i == 10:
           ten += 1
        
        change = i - 5 
        if change == 5:
            if five > 0:
                five -= 1
            else:
                return False
        elif change == 15:
            if five > 0 and ten > 0:
                five -= 1
                ten -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
            
    return True

# print(lemonade_change([5,5,5,10,20])) 
                
                
                
# valid parenthesis - [lc - 678]
def valid_pars(s):
    low = 0    
    high = 0
    
    for i in s:
        if i == '(':
            low += 1
            high += 1
            
        elif i == ')':
            low -= 1
            high -= 1
        
        elif i == "*":
            low -= 1
            high += 1
        
        if high < 0:
            return False
        if low < 0:
            low = 0
        
    return low == 0


# print(valid_pars("(*))"))



# jump one - [lc - 55]
def jump(arr):
    
    reach = arr[0]
    
    for i in range(1, len(arr)):
        if i > reach:
            return False
        else:
            reach = max(reach, i + arr[i])
        
    return reach >= len(arr) - 1
        
# print(jump([2, 3, 1, 1, 4]))    



# jump game - [lc - 45]
def jump_game_2(nums):
    
    jumps = 0
    end = 0
    reach = 0
    
    for i in range(len(nums) - 1):
        reach = max(reach, i + nums[i])
        
        if i == end:
            jumps += 1
            end = reach
            
    return jumps

# print(jump_game_2([2, 3, 1, 1, 4])) 



# Minimum number of platforms required for a railway
def train_station(arrival, depart):
    arrival.sort()
    depart.sort()
    
    i = j = 0
    platfroms = 0
    max_platfroms = 0
    
    while i < len(arrival) and j < len(depart):
        
        if arrival[i] <= depart[j]:
            platfroms += 1
            i += 1
        else:
            platfroms -= 1
            j += 1
        
        max_platfroms = max(max_platfroms, platfroms)
        
    return max_platfroms


# print(train_station([900, 940, 950, 1100], [910, 1200, 1120, 1130]))




def job(deadline, profit):
    
    profit.sort(reverse=True)
    
    max_deadline = max(deadline)
    
    i = j = 0
    
    while i < len(deadline) and j < len(profit):
        if deadline[i] == 
    
    