class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curSum = 0
        hashmap = {0 : 1} # { prefixSum : count}

        for i in range(len(nums)):
            curSum += nums[i]
            diff = curSum - k
            # check if this prefixSum is in hashmap
            if diff in hashmap:
                # if it is, need to update result
                result += hashmap[diff]
            # regardless if prefixSum in or not in hashmap, need to update count of diff
            hashmap[curSum] = 1 + hashmap.get(curSum, 0)
        return result