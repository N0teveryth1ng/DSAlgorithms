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


# Recursion - print name 5 times
def rec(maxs, current=1):
    if current >= maxs:
        return current
    print(current)
    rec(maxs, current + 1)
    
# rec(5)



def recs(i, n):
    if i < n:
        return
    print(i)
    recs(i-1, n)
    
# recs(7,0)        



def rec2(i, n):
    if i < n:
        return
    print(i)
    rec2((i*1) - 1, n)
    
# rec2(7,0)


def sums(i, sum=0):
    if i < 1:
        return sum
    
    return sums(i-1, sum + i)
    
# print(sums(5))


def nums(i, n):
    if i < n:
        return 
    print(i)
    nums(n,i + 1)
    
# nums(0,7)


# not done until dead 
# prints 1 to n 
def process(i, n):
    if i > n:
        return i
    print(i)
    process(i+1,n)
    
# process(0,7)


# N to 1
def rev(i,n):
    if i < n:
        return
    print(i)
    rev(i-1,n)
    
# rev(7,0)        


# print name N times
def nat(i,n):
    if i >= n:
        return
    print('wrick')
    nat(i + 1, n)
    
# nat(0,5)


# sum of first n number
def sums(n):
    if n == 0:
        return 0 
    return n + sums(n-1)
    
# print(sums(3))


# factorial
def fact(n):
    if n == 0: 
        return 1
    return n * fact(n-1)
        
# print(fact(5))


# reverse an array - 2 vars
# def revert(a,x,y):
#     if x >= y:
#         return
#     a[x], a[y] = a[y], a[x]
#     revert(a,x+1, y-1)    
    
# arr = [1,2,3,4,5]    
# revert(arr, 0, len(arr) - 1)
# print(arr)    


# single var
# def rev2(a,i,n):
#    if i >= n/2:
#       return 
#    a[i], a[n-i-1] = a[n-i-1], a[i]
#    rev2(a, i+1, n)

# rev2(arr, 0, len(arr))
# print(arr)
    
    
def checkrev(i,n):    
    a = str(input('Str: '))
    if a[i] != a[n-i-1]:
        return False
    checkrev(i+1)
    
# checkrev('hello')



# multple recurs calls

def multirec(n):
    if n <= 1:
        return n
    
    last = multirec(n-1)
    slast = multirec(n-2)    
    return last + slast

# print(multirec(4))


# string plaindrome or not 
def pal(n):
    n = n.lower()
    if n == n[::-1]:
        print('palindrome')
    else:
        print('not palindrome')    
        
# pal('madam')


# two sum 
arr = [10,20,30,40]
def twosum(n, target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
               return True
    return False
    
# target = 50
# if twosum(arr, target):
#     print('valid')
# else:
#     print('not valid')             
           



           
           

