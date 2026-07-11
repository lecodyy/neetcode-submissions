class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;


        int l = 0;


        for (int r = 1; r < prices.size(); r++) {
            if (prices[l] < prices[r]) {
                int profit = prices[r] - prices[l];
                maxProfit = std::max(maxProfit, profit);
            }
            else {
                l = r;
            }

        }
        return maxProfit;
    }
};
