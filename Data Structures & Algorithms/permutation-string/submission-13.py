class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1freq = {} # just s1 character : frequency
        for c in s1:
            s1freq[c] = s1freq.get(c, 0) + 1

        s2freq = {} # first starting characters of s2 from length of s1
        for i in range(len(s1)):
            s2freq[s2[i]] = s2freq.get(s2[i], 0) + 1
        
        print(s1freq)
        print(s2freq)

        
        left = 0
        right = len(s1) - 1

        # Check initial window before sliding
        if s1freq == s2freq:
            return True

        # Slide the window from index len(s1) to the end of s2
        for right in range(len(s1), len(s2)):
            left = right - len(s1)
            
            # Remove character exiting at the left
            s2freq[s2[left]] -= 1
            if s2freq[s2[left]] == 0:
                del s2freq[s2[left]]
                
            # Add character entering at the right
            s2freq[s2[right]] = s2freq.get(s2[right], 0) + 1
            
            # Check for match
            if s1freq == s2freq:
                return True

        return False