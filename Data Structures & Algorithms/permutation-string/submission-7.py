class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_dict = {}
        s2_dict = {}
        left = 0
        right = len(s1)


        if len(s2) < len(s1):
            return False
        
        for i in range(len(s1)):
            s1_dict[s1[i]] = s1_dict.get(s1[i], 0) + 1
            s2_dict[s2[i]] = s2_dict.get(s2[i], 0) + 1

        for right in range(len(s1), len(s2)):
            if s1_dict == s2_dict:
                print(f"Dict 1 in loop {left}: {s1_dict}")
                print(f"Dict 2 in loop {left}: {s2_dict}")
                return True
            else:

                s2_dict[s2[left]] = s2_dict.get(s2[left], 0) - 1
                if s2_dict[s2[left]] == 0:
                    del s2_dict[s2[left]]
                left += 1
                s2_dict[s2[right]] = s2_dict.get(s2[right], 0) + 1

        return s1_dict == s2_dict

        

