class Solution {
    public int numEnclaves(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        Queue<int[]> q = new LinkedList<>();
        for (int j=0;j<m;j++) {
            if (grid[0][j] == 1) {
                q.add(new int[]{0,j});
                grid[0][j] = 0;
            }
            if (grid[n-1][j] == 1) {
                q.add(new int[]{n-1,j});
                grid[n-1][j] = 0;
            }
        }
        for (int i=0;i<n;i++) {
            if (grid[i][0] == 1) {
                q.add(new int[]{i, 0});
                grid[i][0] = 0;
            }
            if (grid[i][m-1] == 1) {
                q.add(new int[]{i,m-1});
                grid[i][m-1] = 0;
            }
        }
        int row_x[] = {-1, 0, 1, 0};
        int col_x[] = {0, -1, 0, 1};
        while (!q.isEmpty()) {
            int x[] = q.poll();
            int i = x[0];
            int j = x[1];
            for (int k=0;k<4;k++) {
                int nr = i + row_x[k];
                int nc = j + col_x[k];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == 1) {
                    q.add(new int[]{nr, nc});
                    grid[nr][nc] = 0;
                }
            }
        }
        int cnt = 0;
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                if (grid[i][j] == 1) cnt++;
            }
        }
        return cnt;
    }
}
