class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.size() != t.size()) {
            return false;  // end early if size isn't equal
        }

        std::unordered_map<char, int> first;
        std::unordered_map<char, int> second;

        for (int i = 0; i < s.size(); i++) {
            if (first.count(s[i]) > 0) {
                first[s[i]]++;
            }
            else {
                first.insert({s[i], 1});
            }

            if (second.count(t[i]) > 0) {
                second[t[i]]++;
            }
            else {
                second.insert({t[i], 1});
            }

        }

        for (auto it = first.begin(); it != first.end(); it++) {
            if (second.find(it->first) == second.end()) {
                return false;
            }

            if (second[it->first] != it->second) {
                return false;
            }
        }

        return true;
    }
};
