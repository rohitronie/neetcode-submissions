class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r=0,1
        for r in range(r, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]
        return l+1