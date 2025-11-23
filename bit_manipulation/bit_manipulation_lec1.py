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
    



     