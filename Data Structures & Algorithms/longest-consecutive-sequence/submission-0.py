class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        set_nums = set(nums)
        for num in set_nums:
            if num - 1 not in set_nums:
                # Start of a sequence
                sequence_number = num
                count = 0
                while sequence_number in set_nums:
                    count += 1
                    sequence_number += 1
                longest_sequence = max(longest_sequence, count)
        
        return longest_sequence

