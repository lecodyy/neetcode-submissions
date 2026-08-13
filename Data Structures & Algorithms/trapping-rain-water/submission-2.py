class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        result = 0

        while l < r:
            if maxL < maxR:
                # left pointer moves to the right.
                # first, check if this is a new maxHeight
                # then, subtract maxHeight to the actual height we are at. 
                # if maxHeight is the same as the actual height we are at, then can't add water
                # but, if maxHeight is bigger than actual height we are at, we can add water
                l += 1
                maxL = max(maxL, height[l])
                result += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                result += maxR - height[r]
        return result