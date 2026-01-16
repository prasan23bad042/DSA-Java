class Solution {
    public int perfectSum(int[] nums, int target) {
        int n = nums.length;
        int mod = 1000000007;
        int[][] dp = new int[n + 1][target + 1];
        dp[0][0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= target; j++) {
                dp[i][j] = dp[i - 1][j];
                if (nums[i - 1] <= j) {
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - nums[i - 1]]) % mod;
                }
            }
        }
        return dp[n][target];
    }
}
