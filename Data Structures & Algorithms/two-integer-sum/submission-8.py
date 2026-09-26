class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i, j]

        # hashmap = {}
        # for i in range(len(nums)):
        #     hashmap[target-nums[i]] = i
        
        # for i in range(len(nums)):
        #     if nums[i] in hashmap and hashmap[nums[i]] != i:
        #         return [i, hashmap[nums[i]]]


        prevMap = {}
        for i, n in enumerate(nums):
            if target-n in prevMap:
                return [prevMap[target-n], i]
            prevMap[n] = i