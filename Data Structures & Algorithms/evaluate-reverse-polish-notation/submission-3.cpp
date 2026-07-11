class Solution {
public:
    int evalRPN(vector<string>& tokens) {

        std::stack<int> intStack;

        for (auto& t: tokens) {
            if (t != "+" && t != "-" && t != "*" && t != "/") {
                intStack.push(std::stoi(t));
            }
            else {
                int right = intStack.top();
                intStack.pop();
                int left = intStack.top();
                intStack.pop();

                if (t == "+") {
                    intStack.push(left + right);
                }
                else if (t == "-") {
                    intStack.push(left - right);
                }
                else if (t == "*") {
                    intStack.push(left * right);
                }
                else {
                    intStack.push(left / right);
                }
            }
        }

        return intStack.top();
    }
};
