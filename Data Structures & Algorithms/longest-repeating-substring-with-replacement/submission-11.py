class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        result = 0

        for right in range(len(s)):
            # add current character into hashmap. if it exists, do + 1
            count[s[right]] = count.get(s[right], 0) + 1
            # determine the count of the highest occuring character
            maxFreq = max(count.values())
            # determine our current windowLength
            windowLength = (right - left + 1)

            # formula. if our current windowLength - maxFreq exceeds k, we need to shrink the window
            while (windowLength - maxFreq > k):
                # remove this count from hashmap
                count[s[left]] -= 1
                # increment left
                left += 1
                # recalculate windowLength
                windowLength = (right - left + 1)
            
            # result is our maxWindowlength we see
            # sometimes the while loop will never run since there are cases where the windowLength - maxFreq never exceeds k. make sure its outside the while loop

            result = max(result, windowLength)

        return result
