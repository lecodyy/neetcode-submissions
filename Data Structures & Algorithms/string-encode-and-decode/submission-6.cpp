class Solution {
public:

    string encode(vector<string>& strs) {
        std::string result;
        for (const auto& s : strs) {
            result += to_string(s.length()) + "#" + s;
        }

        return result;

    }

    vector<string> decode(string s) {
        std::vector<string> result;
        int i = 0;

        while (i < s.size()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int len = std::stoi(s.substr(i, j - i));
            result.push_back(s.substr(j + 1, len));
            i = j + len + 1;
        }

        return result;


    }


};
