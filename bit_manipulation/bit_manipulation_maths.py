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
    
    if n <= 2:
        return 0
    
    prime = [True] * n
    prime[0] = prime[1] = False
    
    p = 2
    while p*p < n:
        if prime[p]:
            for i in range(p*p, n, p):
                prime[i] = False
            p+=1
            
    return sum(prime)

# print(sieve(1))



# smallest prime factor - - - most third class Q's ever i have done so far 
def smalles_prime_factor(n):
    
    spf = [0] * (n+1)
    
    for i in range(2, n+1):
        if spf[i] == 0:
            spf[i] = i
            for j in range(i*i, n+1, i):    
                if spf[j] == 0:
                    spf[j] = i
                    
    return spf

# print(smalles_prime_factor(8))



    
# power(n,x) - - - - still needs to be cleared 
def pow(x,n):
    
    def helper():
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        res = helper(x, n // 2)
        res = res * res
        
        return x * res if n % 2 else res 
    
    res = helper(x, abs(n))
    return res if n >= 0 else 1/res 
    


