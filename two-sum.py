class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for index, num in enumerate(nums):
            if target - num in ans:
                return [ans[target-num], index]
            ans.update({num: index})