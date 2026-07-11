class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hashtable;

        for (int i = 0; i < nums.size(); i++) {
            int complement = target - nums[i];

            if (hashtable.find(complement) != hashtable.end()) {
                return {hashtable[complement], i};
            }

            hashtable.insert({nums[i], i});
        }

        return {};
    }
};
