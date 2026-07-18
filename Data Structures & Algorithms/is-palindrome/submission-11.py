class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = "".join(char for char in s if char.isalnum()) # i looked this up, list comprehension loop
        print(text)
        l = 0
        r = len(text) - 1

        while l < r:
            if text[l].lower() != text[r].lower():
                return False
            else:
                print(f"l: {text[l]}")
                print(f"r: {text[r]}")
                l += 1
                r -= 1
        return True
