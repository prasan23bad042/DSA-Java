class Solution {
    public int knapsack(int W, int val[], int wt[]) {
        int n = val.length;
        int[][] dp = new int[n + 1][W + 1];

        for (int i = 1; i <= n; i++) {
            for (int w = 0; w <= W; w++) {

                dp[i][w] = dp[i - 1][w];  // not take item

                if (wt[i - 1] <= w) {
                    dp[i][w] = Math.max(
                        dp[i][w],
                        val[i - 1] + dp[i - 1][w - wt[i - 1]]
                    );
                }
            }
        }

        return dp[n][W];
    }
}
