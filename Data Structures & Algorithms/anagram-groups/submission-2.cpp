class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::unordered_map<std::string, vector<string>> freqMap;

        for (const auto& s : strs) {
            std::string sorted = s;
            sort(sorted.begin(), sorted.end());
            freqMap[sorted].push_back(s);
        }

        std::vector<vector<string>> result; 
        for (const auto& pair : freqMap) {
            result.push_back(pair.second);
        }

        return result;
    }
};
