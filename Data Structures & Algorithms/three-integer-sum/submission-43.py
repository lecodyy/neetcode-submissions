class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        # [-4, -1, -1, 0, 1, 2]

        # variable left will iterate through nums
        # variable middle will be in between left and right
        # variable right will always be len(nums) - 1
        
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:
                # not a valid left. skip until fresh nums
                continue
            middle = left + 1
            right = len(nums) - 1
            while middle < right:
                triplet_sum = nums[left] + nums[middle] + nums[right]
                if triplet_sum == 0:
                    # found triplet
                    results.append([nums[left], nums[middle], nums[right]])
                    middle += 1
                    right -= 1
                    # find new triplet
                    while middle < right and nums[middle] == nums[middle - 1]:
                        middle += 1
                    while middle < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif triplet_sum < 0:
                    middle += 1
                else:
                    right -= 1
        
        return results


