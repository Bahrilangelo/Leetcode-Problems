def containsDuplicate(nums):
    hashNums = {}
    for index, i in enumerate(nums):
        if i not in hashNums:
            hashNums.update({i:index})
            print(i)
        else:
            return True
        
    return False
    
print(containsDuplicate([1,2,3,1]))