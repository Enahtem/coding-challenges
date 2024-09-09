class Solution(object):
    def intersect(self, nums1, nums2):
        num1counts = {}
        for num in nums1:
            if num in num1counts:
                num1counts[num]+=1
            else:
                num1counts[num]=1
        
        intersection = []
        for num in nums2:
            if num in num1counts and num1counts[num]>0:
                num1counts[num]-=1
                intersection.append(num)
        return intersection


