# remove duplicates from sorted array

class Solution(object):
    def removeDuplicates(self,nums):
        if not nums:
            return 0
        slow = 0
        for fast in range(1, len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

sol = Solution()
nums = [1, 1, 2, 2, 2, 3, 5, 5,4]
new_length = sol.removeDuplicates(nums)
print("Array after removing duplicates:", nums[:new_length])


 
