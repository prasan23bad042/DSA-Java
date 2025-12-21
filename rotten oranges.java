class Solution {
    public int orangesRotting(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int fresh = 0;

        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[i].length; j++){
                if(grid[i][j] == 1) fresh++;
                else if(grid[i][j] == 2) q.add(new int[]{i, j, 0});
            }
        }

        int max_t = 0;
        int row_x[] = {-1, 0, 1, 0};
        int col_x[] = {0, -1, 0, 1};

        while(!q.isEmpty()){
            int x[] = q.poll();
            int row = x[0];
            int col = x[1];
            int t = x[2];
            max_t = t;

            for(int i = 0; i < 4; i++){
                if(row + row_x[i] >= 0 &&
                   row + row_x[i] < grid.length &&
                   col + col_x[i] >= 0 &&
                   col + col_x[i] < grid[0].length &&
                   grid[row + row_x[i]][col + col_x[i]] == 1){

                    q.add(new int[]{
                        row + row_x[i],
                        col + col_x[i],
                        t + 1
                    });

                    grid[row + row_x[i]][col + col_x[i]] = 2;
                    fresh -= 1;
                }
            }
        }

        if(fresh > 0){
            return -1;
        }
        return max_t;
    }
}
