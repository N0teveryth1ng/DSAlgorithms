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
# print(keep_fact(60))


# print all divisors of a number
def all_divisors(n):
    
    store = []
    i = 1
    
    while i*i <= n:
        if n % i == 0:
            store.append(i)
            if i != n // i:
                store.append(n // i)
        i += 1 
            
    return store
        
# print(all_divisors(60))



# print all divisors optimal 
def print_all_divs(n):
   
   small = []
   big = []
   i = 1
   
   while i * i <= n:
        if n % i == 0:
            small.append(i)
            if i != n // i:
               big.append(n//i)
        i+=1
        
   return small + big[::-1] 
    
# print(print_all_divs(60))



# LC - 1492
def kth_factor_of_n():
    n = 12
    k = 3
    
    small = [] 
    big = []
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            small.append(i)
            if 1 != n // i:
                big.append(n//i)    
        i+=1
        
    big.reverse()
    factor = small + big
    return factor[k-1] if k <= len(factor) else -1

# print(kth_factor_of_n())


# sieve of eratosthenes - - - - - count all primes 
def sieve(n):
    
    prime = [True] * (n+1)
    prime[0] = prime[1] = False
    p = 2
    
    while p*p <= n:
        if prime[p]:  
            for i in range(p*p, n+1, n):
                prime[i] = False
        p += 1
        
    return [i for i in range(n+1) if prime[i]]

# print(sieve(10))


