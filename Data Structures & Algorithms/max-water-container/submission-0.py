class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        l, r = 0, len(heights) - 1
        while l < r:
            width = r-l 
            height = min(heights[l], heights[r])
            if heights[l] == height:
                l += 1
            else:
                r -= 1
            curr_area = width * height
            area = max(area, curr_area)
        return area