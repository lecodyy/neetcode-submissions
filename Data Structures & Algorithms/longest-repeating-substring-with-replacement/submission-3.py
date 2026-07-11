class Solution: 
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        result = 0
        left = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            window_len = right - left + 1
            largest_count = max(counts.values())

            while window_len - largest_count > k:
                counts[s[left]] -= 1
                left += 1
                window_len = right - left + 1
                largest_count = max(counts.values())

            result = max(window_len, result)

        
        return result