# I will continue to solve problems of monotnic stacks and queues

# LC - 496 
def next_gret():

    n1 = [4, 1, 2]
    n2 = [1, 3, 4, 2]
    
    stack = []
    
    for num in n1:
        found = -1
        
        for i in range(len(n2)):
            if n2[i] == num:
                
                for j in range(i+1, len(n2)):
                    if n2[j] > i:
                        found = n2[j]
                        break    
                break
            
        stack.append(found)
    return stack
    

# print(next_gret())



def next_great_elem(num1, num2):
    
    stack = []
    mappo = {}
    
    for i in reversed(num2):
        while stack and stack[-1] <= i:
            stack.pop()
            
        if stack:
            mappo[i] = stack[-1]
        else:
            mappo[i] = -1
            
        stack.append(i)
        
    return [mappo[n] for n in num1]
    
# print(next_great_elem([4,1], [1,2,3,4]))

            
            
            