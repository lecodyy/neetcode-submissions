class Solution {
public:
    void backtrack(int open, int closed, int n, vector<string>& res, std::string& stack) {
        // add open if open < n
        // add closed if closed < open
        // base case: a stack is created when open == closed == n

        if (open == closed && open == n) {
            res.push_back(stack);
            return;
        }

        if (open < n) {
            stack += '(';
            backtrack(open + 1, closed, n, res, stack);
            stack.pop_back();
        }

        if (closed < open) {
            stack += ")";
            backtrack(open, closed + 1, n, res, stack);
            stack.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string> res;
        std::string stack;

        backtrack(0, 0, n, res, stack);
        return res;
    }
};
