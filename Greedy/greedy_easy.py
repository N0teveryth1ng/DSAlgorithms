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



# lemonade change 
def lemonade_change():
    
    