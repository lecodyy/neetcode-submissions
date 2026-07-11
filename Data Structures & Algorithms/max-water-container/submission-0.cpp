class Solution {
public:
    int maxArea(vector<int>& heights) {
        int max = INT_MIN;
        int temp = 0;

        int l = 0;
        int r = heights.size() - 1;

        while (l < r) {
            temp = std::min(heights[l], heights[r]) * (r - l);
            max = std::max(max, temp);

            if (heights[l] > heights[r]) {
                r--;
            }
            else {
                l++;
            }
        }

        return max;
    }
};
