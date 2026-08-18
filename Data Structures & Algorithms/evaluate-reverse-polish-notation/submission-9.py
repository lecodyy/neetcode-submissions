class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        operators = {"+", "-", "*", "/"}
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:

                second = stack.pop()
                first = stack.pop()

                if tokens[i] == "+":
                    temp = first + second
                    stack.append(temp)
                if tokens[i] == "-":
                    temp = first - second
                    stack.append(temp)
                if tokens[i] == "*":
                    temp = first * second
                    stack.append(temp)
                if tokens[i] == "/":
                    temp = int(first / second)
                    stack.append(temp)
                        
        
        return stack.pop()
                
