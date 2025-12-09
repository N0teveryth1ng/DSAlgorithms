# BIT MANIPULATION Math's part 

# prime number checker  - - - -  
def is_prime(n):
    
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False            
    
    return True
# print(is_prime(9))



# print the prime factors
def prime_factors(n):
    factors = []
    
    for i in range(2, n+1):
       if  n % i == 0 and is_prime(i):
            factors.append(i)
              
    return factors

# print(prime_factors(60))


# keep on divide until one number is exhausted 
def keep_fact(n):
    store = []
    i = 2
    
    while i * i <= n: 
        if n % i == 0:
            store.append(i)
            while n % i == 0:
                n = n // i        
        i+=1
        
    if n > 1:
        store.append(i) 

    return store
print(keep_fact(60))


# 