class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1
        suffix = [0] * len(nums)
        suffix[len(nums) - 1] = 1

        # prefix loop. multiply everything to the left of i.
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        print(prefix)

        # suffix loop. multiply everything to the right of i. loop backwards
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            print(suffix[i])
        print(suffix)

        result = []
        for i in range(len(nums)):
            result.append(prefix[i] * suffix[i])

        return result








