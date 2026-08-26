class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # use a stack to loop through the rectangles
        # store its (value, index)
        # if stack empty, push first rectangle ot stack
        # if the next rectangle is equal or bigger, add that one to the stack
        # if the next rectangle is smaller, we cannot extend further w our current height
        # so we check. check the top of the stack (should be previous rectangle)
        # calculate its area. height x width (popped value x (i - popped index))
        # compare that to max height
        # then continue going left. check if the each next rectangle is less or equal than the rectangle at i
        # if so, this is the max that rectangle we stopped at i can go.
        # stop popping, add (height of height[i], index we stopped at) to stack
        # do this until we reach the end of hte array. not done yet
        # there are still elements in the array, all in increasing order
        # start at top of stack. calculate its area by looping
        # max width is just len(heights) - popped_index)
        # height x width (popped height x len(heights) - popped_index)
        # take each max per loop
        # max is confirmed

        stack = deque()
        # store values in stack as (height, index)
        maxArea = 0

        for i in range(len(heights)):
            if len(stack) == 0:
                stack.append((heights[i], i))
                continue
            
            new_start = i
            cur_h = heights[i]
            while stack and cur_h < stack[-1][0]:
                #calculate height
                prev_h, prev_i = stack.pop()
                maxArea = max(maxArea, prev_h * (i - prev_i))
                new_start = prev_i

            stack.append((cur_h, new_start))

        # post stack checking
        total_width = len(heights)
        for h, i in stack:
            maxArea = max(maxArea, h * (total_width - i))        
        return maxArea
            
            

