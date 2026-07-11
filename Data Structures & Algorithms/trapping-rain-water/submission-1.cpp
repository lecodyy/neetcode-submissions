class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;

        int maxL = height[l];
        int maxR = height[r];

        int result = 0;

        while (l < r) {
            if (maxL < maxR) {
                //left
                l++;
                maxL = std::max(maxL, height[l]);

                int tempL = maxL - height[l];
                if (tempL > 0) {
                    result += tempL;
                }


            }
            else {
                //right 
                r--;
                maxR = std::max(maxR, height[r]);

                int tempR = maxR - height[r];
                if (tempR > 0) {
                    result += tempR;
                }
            }
        }
        return result;
    }
};
