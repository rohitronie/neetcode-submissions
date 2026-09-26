class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, 0

        for i, n in enumerate(nums):
            if n != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

            right += 1
        return left
    

    