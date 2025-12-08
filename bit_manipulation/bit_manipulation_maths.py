# BIT MANIPULATION Math's part 

# prime number checker  - - - -  
def prime_factors(n):
    
    if n < 2:
        return False
    
    for i in range(2, n):
        if n % i == 0:
            return False
            
    return True

# print(prime_factors(5))


# print the prime factors
def prime_factors():
    
    
