#https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/

class Solution(object):
    def removeDuplicates(self,nums):
        count = 0
        for i in range(len(nums)):
            if (nums[i]>nums[count]):
                count+=1
                nums[i], nums[count] = nums[count], nums[i]
        return count+1
