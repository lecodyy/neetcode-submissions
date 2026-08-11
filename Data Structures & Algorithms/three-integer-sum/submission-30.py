class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        # variable left will iterate through array. 
        # middle will start at 1 above left
        # right will start at len(nums) - 1
        result = []
        test = [-2, 0, 0, 2, 2]
        for left in range(len(nums)- 2):
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                temp = nums[left] + nums[middle] + nums[right]
                if temp == 0:
                    result.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    # go find a different integer to start
                    while middle < right and nums[middle] == nums[middle - 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif temp < 0:
                    # negative answer. move middle one to the right
                    middle += 1
                else:
                    # positive ansewr. move right one to the left
                    right -= 1
        return result

                    


            