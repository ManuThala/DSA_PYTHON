def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) == sorted(s2):
        return True

s1='hello'
s2='lloeh'
res=anagram(s1,s2)
if res==True:
    print('anagram')
else:
    print('not an anagram')
