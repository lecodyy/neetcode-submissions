class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        std::stack<pair<int,int>> stack; // temp, index
        std::vector<int> result(temperatures.size(), 0);

        for (int i = 0; i < temperatures.size(); i++) {
            int temp = temperatures[i];
            while (!stack.empty() && temp > stack.top().first) {
                    result[stack.top().second] = i - stack.top().second;
                    stack.pop();
            }

            stack.push({temp, i});


        }

        return result;

    }
};
