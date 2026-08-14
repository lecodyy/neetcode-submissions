class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # {sorted string: list of anagrams}
        hashmap = {}
        for string in strs:
            # sort the string.
            sorted_string = "".join(sorted(string))
            if sorted_string in hashmap:
                # in hashmap, add string to value which is a list
                hashmap[sorted_string].append(string)
            else:
                hashmap[sorted_string] = [string]
            
        result = list(hashmap.values())
        return result
