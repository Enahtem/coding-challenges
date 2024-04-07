# https://leetcode.com/problems/two-sum/description/

def twosum(nums, target):
    indices = {} #Hashmap for fast retrieval
    for i in range(len(nums)): #O(n)
        if (target-nums[i] in indices): #O(1)
            return [indices[target-nums[i]],i]
        indices[nums[i]]=i


print(twosum([12,5,2,5,7,2,35], 42))