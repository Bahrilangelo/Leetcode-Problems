def isPalindrome(s):
    ans = ''
    for i in s:
        if i.isalnum() == True:
            ans += i.lower()
    return ans == ans[::-1]

print(isPalindrome('race a car'))