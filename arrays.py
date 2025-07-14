# 1. pattern printing
def pattern(n): 
  for i in range(1,n):
    for j in range(1,n):
          print('* ', end=" ")
    print() 

# pattern(n = 10)



# 2. Q
def pattern1(n):
    for i in range(0,n):
        for j in range(0,i):
            print("* ", end='')
        print()
        
# pattern1(n=6)    
    
    
# 3. Q     
def pattern3(n):
    for i in range(1,n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
        
# pattern3(5)    


# 4. Q
def pattern4(n):
    for i in range(1,n+1):
        for j in range(n, i+n):
            print(i, end=" ")
        print()
        
# pattern4(5)    

  
#  5. Q    
def pattern5(n):
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()
        
# pattern5(n=6)


# 6
def patter6(n):
 for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print() 
 
# patter6(5)   
       
        
# 7 - pyramid pattern
def pattern7(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(2*i-1):
            print("*", end=" ")    
        print()
        
# pattern7(5)


 
# 8 - upside down pyramid
def pattern8(n):
    for i in range(n,0,-1):
        for j in range(n-i):
            print(" ", end=" ")
        for k in range(2*i-1):
            print("*", end=" ")
        print()
        
# pattern8(5)                



# 9 - rhombus
def pattern9(n):
  for i in range(0, n+1):
      print(" " * (n-i) + "*" * (2*i-1))
  for j in range(n-1,0,-1):
      print(" " * (n-j) + "*" * (2*j-1))
  print()  
    
# pattern9(7)

    
# 10 - 
def pattern10(n):
  for i in range(0,n+1):
      print("*" * i)
  for j in range(n-1,0,-1):
      print("*" * j)    
      
# pattern10(5)


def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example
# print("GCD is:", euclid_gcd(48, 18))  # Output should be: GCD is: 6

# import math 
# x = 4
# count = []
# x = abs(x)
        
# for i in range(1, math.sqrt(x)):
#     if x % i == 0 and x // i == 0:
#         count.append(i)
    
# print(count)


# Recursion
def rec(maxs, current=1):
    if current >= maxs:
        return current
    print('soham')
    rec(maxs, current + 1)
    
# rec(10)



def fact(n):
  result = 1 
  for i in range(1, n+1):
     result = result * i
  return result  
    
print(fact(5))    