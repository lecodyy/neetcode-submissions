class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int> freqMap;

        for (int i = 0; i < nums.size(); i++) {
            freqMap[nums[i]]++;
        }

        std::vector<std::pair<int, int>> vec;

        for (const auto&[key, value] : freqMap) {
            vec.push_back({value, key});
        }
    std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b) {
        return a.first > b.first; // frequency is now second
    });

        vector<int> result;

        for (int i = 0; i < k; i++) {
            result.push_back(vec[i].second);
        }

        return result;

    }
};
