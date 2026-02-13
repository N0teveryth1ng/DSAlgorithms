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



