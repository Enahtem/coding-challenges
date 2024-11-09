class Solution(object):
    def moveZeroes(self, nums):
        zerosPassed = 0
        for i in range(len(nums)):
            if (nums[i]==0):
                zerosPassed+=1
            else:
                nums[i], nums[i-zerosPassed] = nums[i-zerosPassed], nums[i]
