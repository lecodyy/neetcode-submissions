class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        # preffix. iterate left to right. at each index, calculate previous indexs' product
        # ex: [1,2,4,6]
        # prefix: [1, 1, 2, 8]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # suffix. iterate right to left. at each index, calculate previosu indexs' product
        # ex: [1,2,4,6]
        # suffix: [48, 24, 6, 1]

        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]


        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])
        
        return result
