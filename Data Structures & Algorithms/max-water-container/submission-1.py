class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        curHeight = 0
        maxHeight = 0

        while l < r:
            curHeight = min(heights[l], heights[r]) * (r - l)
            maxHeight = max(curHeight, maxHeight)
            if heights[l] > heights[r]:
                # right pointer moves left
                r -= 1
            else:
                # left pointer moves right
                l += 1
        return maxHeight
