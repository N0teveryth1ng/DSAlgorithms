# bit manipulaton lect 1

# convert decimal to binary ------- divide + collect remainders
def convert_binary(n):
    
    if n == 0:
        return "0"
    
    res = ""
    while n > 0:
        res += str(n % 2)
        n //= 2
        
    return res[::-1]

# print(convert_binary(13)) # output - 1011


# convert binary to decimal ------------ multiply + accumulate
def convert_decimal(n):
    
    res = 0
    for i in n:
        res = res * 2 + int(i)
    return res

# print(convert_decimal("1011"))
    


# if i is 1 then its set if 0 then not  
def set_not(n, i):
    
    if n & ( 1 << i) != 0:
        print("1 is set")
    else:
        print("0 is not set")
    
    
# print(set_not(13,1))
    
    
def right_shift(n, i):
        
    if n & ( 1 >> i) != 0:
        print("1 is set")
    else:
        print("0 is not set")

# print(right_shift(13,3))


# clear the ith bit
def clear_ith(n, i):
    
    if n & ~(1 << i) != 0:
        print(f"{i} is set")
    else:
        print("not set")
        
# print(clear_ith(13,3))


# toggle the ith bit
def toggle_bit(n,i):
    return n ^ ( 1 << i)

# print(toggle_bit(13,2))


# remove the last set bit
def remove_last_bit(n):
    return n & (n-1)

# print(remove_last_bit(13))


# check if the num is power of 2 or not
def check_pow(n):
    
    if n & (n-1) == 0:
        print(f"{n} True")
    else:
        print(f"{n} False")
        
# print(check_pow(13))



# count the number of set bits
def count_numset_bits(n):
    
    cnt = 0
    while n > 0:
        if n % 2 == 1:
            cnt += 1
        n = n//2
           
    return cnt
    
# print(count_numset_bits(15))



# swap the nums of two
def swap_nums(a,b):
    swap = a,b = b,a
    return swap

# print(swap_nums(2,3))


# divide 2 nums without dividing opt
def divide_opt(n, d):
    
    if n == d:
        return 1
    
    sign = not ((n < 0) ^ (d < 0))
    
    n = abs(n)
    d = abs(d)
    
    ans = 0
    
    while n >= d:
        
        temp = d
        cnt = 1
        
        while temp << 1 <= n:
            temp <<= 1
            cnt <<= 1
            
        n -= temp
        ans += cnt
        
    ans = ans if sign else -ans
    
    int_max = 2**31 - 1
    int_min = -2**31
    
    if ans < int_min:
        return int_min
    if ans > int_max:
        return int_max
        
    return ans

# print(divide_opt(43,7))


