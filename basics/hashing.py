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
    
    
    
    
    
    
    
# _ _ _ _ _ _ _ _ _ _ _ _ 
# basic follower counter | - using HASHING
# - - - - - - - - - - - -
 
# user = str(input('enter name: '))
# followers = {}
# current_followers = {
#     "alex",
#     "lola",
#     "man",
#     "sonic", 
#     "dash"
# }

# new_follower = "polo"
      
# checks total followers
# def check_followers():
#      for name in current_followers:
#          followers[name] = True
         
#      if new_follower in followers:
#          print('exists') 
#      else:
#          followers[new_follower] = True
#          print('added')
#          print(followers)
#          print(f"{user}'s total follower is - ", len(followers))    
  

# insert follower
# def insert_followers():
#     select_insert = str(input('enter name to insert - '))
#     current_followers.add(select_insert) 
#     print(f"{select_insert} added to followers")
  
# # delete followers
# def del_followers():
#     select_del = str(input("Enter delete user name: "))
#     if select_del in current_followers:
#         current_followers.remove(select_del)
#         print(f"{select_del} has been removed")
#     else:
#         print(f"{select_del} is not a follower") 
        

# # calling fucntions
# check_followers()
# insert_followers()
# del_followers()

# # show final followers
# print(f"final list - {current_followers}")


# character hashing
# arstr = ["a","a","b","n","d"]

def charlook(arstr):
    count = {}
    
    for i in arstr:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
    return count        
    
    
# print(charlook(arstr))        

# def look 
chers = ["a","a","b","b","x"]

def chlook(chers):
    counts = {}
    for ch in chers:
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
            
    return counts

# print(chlook(chers))    
             
    
# number hashing

arr = [1,3,4,5,6]
def numhash():    
    count = {}
    for i in arr:
       if i in count:
          count[i] += 1
       else:
           count[i] = 1
           
    return count
          

# print(numhash())

        
# odd/even frequescy

Input = [2, 3, 2, 4, 4, 3, 5]
def check(Input):
   store = {}
   for i in Input:
      if i in store:
          store[i] += 1
      else:
          store[i] = 1
    
   for j in store:
        if store[j] % 2 != 0:
            return j
   
# print(check(Input))      



# anagram check
s = "listen"
t = "silent"
def check(s,t):
   if len(s) != len(t):
        return False
    
   store = {}
   
   for i in s:
          store[i] = store.get(i, 0) + 1
    
   for j in t:
        if j not in store or store[j] == 0:
            return False
        store[j] -= 1
        
   return True
        
# print(check(s,t))   











# - - - - - - division method - array hashing - - - - - - - 

# Array hashing with sorting elements
arr = [2,3,4,5,5,5,5,6,7,8,8,8,8,8,8,9,45,74,89,98]
table_size = 10
hash_table = {i: [] for i in range(table_size)}

# storing
def store(arr):
  for i in arr:  
     hash_key = i % table_size
     bucket = hash_table[hash_key] # prevent collision
     
     bucket.append(i)
     

# searching
def search(n): 
    hash_key = n % table_size
    bucket = hash_table[hash_key]
    return n in bucket

store(arr)
store([37])


# sorting
frequency = {}

for bucket in hash_table.values():
    for i in bucket:
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
       
if not frequency:
    print(" not in the table")
else:
    
    max_freq = max(frequency.values())
    min_freq = min(frequency.values())
    
    highest_freq = [i for i,j in frequency.items() if j == max_freq]
    lowest_freq = [i for i,j in frequency.items() if j == min_freq]
    
    print("freqs elems are : ", frequency)
    print("highest highs: ", highest_freq, "max freqs: ", max_freq)
    print("lowest lows: ", lowest_freq, "min freqs: ", min_freq)
    
    
    