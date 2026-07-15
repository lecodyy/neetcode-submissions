class Solution:

    def encode(self, strs: List[str]) -> str:
        # length of string, delimiter, string itself
        result = ""
        for string in strs:
            result += str(len(string)) +"#"+ string
        return result


    def decode(self, s: str) -> List[str]:
        print(s)
        result = []
        length = 0
        i = 0
        j = 0
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] == "#":
                    length = int(s[i:j])
                    break
                j += 1
            result.append(s[j+1:j+1+length])
            i = j + 1 + length
        return result


