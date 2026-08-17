class Solution {

    // Returns the maximum score Alice can obtain from stones[i...j].
    public int game(int dp[][], int a[], int i, int j, int total) {

        // With one or zero stones, no split is possible.
        if (i >= j) return 0;

        // Return the already computed result for this interval.
        if (dp[i][j] != -1) return dp[i][j];

        int ans = 0;

        // Sum of the left part while moving the split point.
        int sum_tillk = 0;

        // Try every possible split:
        // [i ... k] | [k+1 ... j]
        for (int k = i; k < j; k++) {

            sum_tillk += a[k];

            // Since total is the sum of a[i...j],
            // the right sum can be obtained in O(1).
            int sum_afterk = total - sum_tillk;

            /*
             * Alice can keep only the side having the smaller sum.
             * She also gets that smaller sum as her score.
             */
            if (sum_tillk > sum_afterk) {

                // Right side is smaller, so Alice continues with it.
                ans = Math.max(
                    ans,
                    sum_afterk + game(
                        dp, a, k + 1, j, sum_afterk
                    )
                );

            } else if (sum_tillk < sum_afterk) {

                // Left side is smaller, so Alice continues with it.
                ans = Math.max(
                    ans,
                    sum_tillk + game(
                        dp, a, i, k, sum_tillk
                    )
                );

            } else {

                /*
                 * Both sides have equal sums.
                 * Alice can choose either side, so take the better option.
                 */
                ans = Math.max(
                    ans,
                    sum_tillk + Math.max(
                        game(dp, a, k + 1, j, sum_afterk),
                        game(dp, a, i, k, sum_tillk)
                    )
                );
            }
        }

        return dp[i][j] = ans;
    }

    public int stoneGameV(int[] stoneValue) {

        int n = stoneValue.length;

        int dp[][] = new int[n][n];

        int total_sum = 0;

        // Calculate the total sum and initialize DP.
        for (int i = 0; i < n; i++) {
            total_sum += stoneValue[i];
            Arrays.fill(dp[i], -1);
        }

        // Start with the complete array.
        return game(dp, stoneValue, 0, n - 1, total_sum);
    }
}