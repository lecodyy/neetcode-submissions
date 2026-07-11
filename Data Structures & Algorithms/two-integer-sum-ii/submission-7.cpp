class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {

        std::unordered_map<int, int> freqMap;
        int one_indexed = 1;

        for (int i = 0; i < numbers.size(); i++) {
            int complement = target - numbers[i];

            if (freqMap.count(complement)) {
                return {freqMap[complement] + 1, i + 1};
            } 
            else {
                freqMap[numbers[i]] = i;
            }
        }

        return {};
    }
};
