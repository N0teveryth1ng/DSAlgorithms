# ṣtrings for part - 1 [ basic and easy strings problem ]

# valid parethesis - -  - -  using LIFO method
def valid_par():
    
    s = "()[]{}"
    
    stack = []
    pairs = { ')': '(', ']': '[', '}': '{' }
    
    for i in s:
            
        if i in pairs:
            if stack and stack[-1] == pairs[i]:  # if last elemnt matched with opening to closing its gets removed
                stack.pop()  
            else:
                return False 
        else:
            stack.append(i)     # every opening elems gets added to the stack
            
            
    return True if not stack else False
                
                
# print(valid_par())


# remove the outermost paretheses
def remove_parentheses():
    
    s = "(()())(())"
    count = 0
    res = []
    
    for i in s:
        if i == "(":
            if count > 0:
                res.append(i)
            count += 1
        else:
            count -= 1
            if count > 0:
                res.append(i)
                
    return "".join(res)

# print(remove_parentheses())


            
# reverse a string
def reverse():
    
    s = "the sky is blue"
    
    s.strip()
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)

# print(reverse())



# largest odd nums - -  return the prefix of longest odd strings
def largest_odd():
    
    num = "52"
    for i in range(len(num) - 1, -1, -1):
        
        if int(num[i]) % 2 == 1:
            return num[:i+1]
        
    return ""
      
# print(largest_odd())    
    
  
  
# longest common prefix
def longest_prefix():
    
    strs = ["flower","flow","flight"]
    res = ""
    
    for i in range(len(strs[0])):
      for s in strs:
        if i >= len(strs) or s[i] != strs[0][i]:
            return res 
      res += strs[0][i]   
    return res

# print(longest_prefix())


# isomorpic string  - - - we swap the letter here with another var
def isomorphic():
    
    s = "egg"
    t = "add"
    
    if len(s) != len(t):
        return False
    
    s_to_t = {}
    t_to_s = {}
    
    for i in range(len(s)):
        c1, c2 = s[i], t[i]
        
        # check mapping from s - t
        if c1 in s_to_t:    
            if s_to_t[c1] != c2:
                return False
        else:
            s_to_t[c1] = c2
            
            
        # check mapping from t - s
        if c2 in t_to_s:
            if t_to_s[c2] != c1:
                return False
        else:
            t_to_s[c2] = c1
                
    return True

# print(isomorphic())



# rotate the string
def rotate_str():
    
     s = "abcderickhjj"
     goal = "rick" 
     
     if len(s) != len(goal):
         return False
     return goal in (s + s)
 
# print(rotate_str())
               


#  - - - - valid anagram or not 
def anagram():
    
    s = "anagram"
    t = "nagaram"
    
    if len(s) != len(t):
        return False
    
    s_count, t_count = {}, {}
    
    for i in s:
        s_count[i] = s_count.get(i, 0)
    
    for j in t:
        t_count[j] = t_count.get(j,0)
        
    return s_count == t_count

# print(anagram())



#  - - - - find words contaning char
def contain():
    
    words = ["leet","code"]
    x = "e"
    
    res = []
    n = len(words)
    
    for i in range(n):
        if x in words[i]:
            res.append(i)
        
    return res
        
# print(contain())


# sort characters by frequency 
from collections import Counter
def test():
    
    s = "dZee"
    cnt = Counter(s)
    sorted_chr = sorted(cnt, key=lambda x: cnt[x], reverse=True)
    
    res = ""
    for i in sorted_chr:
        res += i * cnt[i]
        
    return res
    
# print(test())



#  - - Maximum Nesting Depth of the Parentheses
def max_dept_part():
    
  s = "(1+(2*3)+((8)/4))+1"
  
  res = 0
  curr = 0
  
  for i in s:
      if i == "(":
         curr += 1
      elif i == ")":
         curr -= 1
      res = max(res, curr)    
         
  return res

# print(max_dept_part())


#  - - - roman to integer
def roman_integer():
    
    values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
    s = "III"
    count = 0    

    for i in range(len(s) - 1):
         if values[s[i]] < values[s[i+1]]:
             count -= values[s[i]]
         else:
             count += values[s[i]]
             
    return count + values[s[-1]]
             
# print(roman_integer())
                
                
# implement atoi - - - - string to integer transformation
def atoi():
    
    s = " -42"
    
    sign = 1
    res = 0
    
    s = s.strip()
    
    if not s:
        return 0
    
    # check for neg values
    if s[0] == '-' or s[0] == '+':
        if s[0] == "-":
            sign = -1
        s = s[1:]
        
    # check if values isDigit or not
    for i in s:
        if not i.isdigit():
            break
        res = res * 10 + int(i)
    
    res = res * sign
    
    # 
    int_min, int_max = -2**31, 2**31 - 1
    
    if res < int_min:
        return int_min
    elif res > int_max:
        return int_max
    
    return res    
    

# print(atoi())


# count number of substrings
def countSubstrings():
    s = "abcd"
    n = len(s)
    ans = n * (n + 1) // 2  # formula to calculate sub-strings
    return ans
    
# print(countSubstrings())  



# longest palindromic substr ---- without DP
def palindromic():
    
    s = "cbbd"
    
    res = ""
    resLen = 0
    
    for i in range(len(s)):
        
        # check odd length
        left, right = i, i
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            
            if (right - left + 1) > resLen:
                res = s[left:right+1]
                resLen = right - left + 1
            left -= 1
            right += 1
            
            
        # check for even length 
        left, right = i, i+1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > resLen:
                res = s[left:right+1]    
                resLen = right - left + 1
            left -= 1
            right += 1
            
        return res
    
# print(palindromic())
            


# sum of beauty of all substring
def beauty_freq():
    
    s = "aabcb"
    total = 0
    
    for i in range(len(s)):
        freq = [0] * 26
        for j in range(i, len(s)): 
            idx = ord(s[j]) - ord('a')
            freq[idx] += 1
            
            maxf = max(freq)
            minf = min(f for f in freq if f > 0)
            
            total += (maxf - minf)   
        
    return total
            
            
# print(beauty_freq())







