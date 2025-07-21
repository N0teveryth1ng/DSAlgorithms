# hashing example -  
arr = [1,2,3,3,5,8]    
def f(number ,arr):
    count = 0
    for i in arr:
        if i == number:
            count += 1
    return count

# print(f(8, arr))


# brute force
for nums in arr:
    if nums == 9:
        print('found')
        break 



# hashed method
hashed = {}

for num in arr:
    hashed[num] = True
    
if 9 in hashed:
    print('found')
    
# freq counting 
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1    
        
# print(freq)

# operations  - - - -> 
table = {}

# # inserting
# table["val"] = 7
# print(table) 

# # get 
# x = table["val"]
# print(x)

# # delete
# del table["val"]
# print(table)


# set in hashing 
# table = {}
# check = 9

# for num in arr:
#    table[num] = True
    
# if check in table:
#     print("exists")
# else:
#     table[check] = 1
#     print(table)
    
    
# chek for existence

# arrs = [12,33,54,71,34,8]
# data = {}
# look = 29
# for num in arrs:
#     data[num] = True
    
# if look in table:
#     data[look] += 1
#     print('is there')
# else:
#     data[look] = 1
#     print(data) 
    
    
    
# follower counter
followers = {}
current_followers = {
    "alex",
    "lola",
    "man",
    "sonic", 
    "dash"
}

new_follower = "polo" 

for name in current_followers:
    followers[name] = True
    
if new_follower in followers:
    print('exists') 
else:
    followers[new_follower] = True
    print('added')
    print(followers)
    print("total followers - ", len(followers))