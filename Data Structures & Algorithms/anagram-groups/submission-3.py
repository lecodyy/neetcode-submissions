class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            sorted_s = sorted(string)
            sorted_t = tuple(sorted_s)
            if sorted_t in hashmap:
                # value should be a list. add string to list
                hashmap[sorted_t].append(string)
            else:
                hashmap[sorted_t] = [string]

        return list(hashmap.values())


