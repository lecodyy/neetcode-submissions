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

        while 1 + right < len(s2):
            if s1freq == s2freq:
                return True
            else:
                # get rid of current left in s2freq.
                s2freq[s2[left]] -= 1
                # if this freq has reached 0, delete from hashmap
                if s2freq[s2[left]] <= 0:
                    del s2freq[s2[left]]
                # slide left over
                left += 1
                # slide right over
                right += 1
                # add new value from right
                print(right)
                s2freq[s2[right]] = s2freq.get(s2[right], 0) + 1
        return s1freq == s2freq

                
                



