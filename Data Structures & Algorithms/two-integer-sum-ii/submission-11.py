class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            index_sum = numbers[l] + numbers[r]
            if index_sum == target:
                return [l + 1, r + 1]
            if index_sum > target:
                r -= 1
            if index_sum < target:
                l += 1
            
