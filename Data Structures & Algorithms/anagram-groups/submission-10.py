class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {sorted string: list of anagrams}
        hashmap = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in hashmap:
                # add in list
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = [string]
        
        return list(hashmap.values())
