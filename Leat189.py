# Rotate Array

class Solution:
    def rotate(self,nums, k):
        n = len(nums)
        k = k % n 
        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
        return nums

sol=Solution()
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
print(sol.rotate(nums1, k1)) 
nums2 = [-1, -100, 3, 99]
k2 = 2
print(sol.rotate(nums2, k2))