class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif c == ")":
                if len(stack) != 0 and stack.pop() == "(":
                    continue
                else:
                    return False
            elif c == "}":
                if len(stack) != 0 and stack.pop() == "{":
                    continue
                else:
                    return False
            elif c == "]":
                if len(stack) != 0 and stack.pop() == "[":
                    continue
                else:
                    return False
        return len(stack) == 0