# def anagram(s1,s2):
#     if len(s1) != len(s2):
#         return False
    
#     dict1={}
#     dict2={}
    
#     for ch in s1:
#         if ch in dict1:
#             dict1[ch]+=1
#         else:
#             dict1[ch]=1

#     for ch in s2:
#         if ch in dict2:
#             dict2[ch]+=1
#         else:
#             dict2[ch]=1

#     for i in dict1:
#         if i not in dict2 or dict1[i] != dict2[i]:
#             return False
#     return True

# s1='Hello'
# s2='olleH'
# res=anagram(s1,s2)
# if res==True:
#     print('Anagram')
# else:
#     print('strings are not an anagram')

# =============================================

# Second type of code

# def anagram(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     else:
#         return sorted(s1) == sorted(s2)
# s1='Hello'
# s2='olleH'
# res=anagram(s1,s2)
# if res==True:
#     print('Anagram')
# else:
#     print('strings are not an anagram')

# Third type of code
from collections import Counter ;
def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    return  Counter(s1)==Counter(s2)

s1='Hello'
s2='olleH'
res=anagram(s1,s2)
if res==True:
    print('Anagram')
else:
    print('strings are not an anagram')