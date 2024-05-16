# two sum

class Solution:
    def twoSum(self, nums, target):
        num_indices = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_indices:
                return [num_indices[complement], i]
            num_indices[num] = i
        return []

sol=Solution()
nums=[1,1,2,2,3,4,4,4]
target=7

print(sol.twoSum(nums,target))