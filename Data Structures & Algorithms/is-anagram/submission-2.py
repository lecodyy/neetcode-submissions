class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)): # can use t here too doesn't matter
            if s[i] not in s_hashmap:
                s_hashmap[s[i]] = 0
            else:
                s_hashmap[s[i]] = s_hashmap[s[i]] + 1

            if t[i] not in t_hashmap:
                t_hashmap[t[i]] = 0
            else:
                t_hashmap[t[i]] = t_hashmap[t[i]] + 1

        return s_hashmap == t_hashmap
            



