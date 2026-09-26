class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]
        for i, n in enumerate(nums[1:]):
            if count == 0:
                res = n
                count = 1
            elif n != res:
                count -= 1
            else:
                count += 1

        return res