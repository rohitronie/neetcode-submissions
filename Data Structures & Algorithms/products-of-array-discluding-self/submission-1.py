class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        premul=1
        for i in range(len(nums)):
            res[i]=premul
            premul*=nums[i]

        postmul=1
        for i in reversed(range(len(nums))):
            res[i]*=postmul
            postmul*=nums[i]
        return res

