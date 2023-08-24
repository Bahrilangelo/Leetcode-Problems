def isAnagram(s,t):
    hashS = {}
    hashT = {}
    for i in s:
        if i not in hashS:
            hashS.update({i:s.count(i)})
    for i in t:
        if i not in hashT:
            hashT.update({i:t.count(i)})
    return hashS == hashT
    

print(isAnagram('rat', 'tar'))