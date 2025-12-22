class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int [][] vis = new int[n][m];
        int [][] res = new int[n][m];
        Queue<int[]> q = new LinkedList<>();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(mat[i][j] == 0){
                    q.add(new int[]{i,j,0});
                    vis[i][j] = 1;
                }
            }
        }
        int row_x[] = {-1,0,1,0};
        int col_x[] = {0,-1,0,1};
        while(!q.isEmpty()){
            int[] x = q.poll();
            int i = x[0];
            int j = x[1];
            int d = x[2];
            res[i][j] = d;
            for(int k=0;k<4;k++){
                int nr = i+row_x[k];
                int nc = j+col_x[k];
                if(nr >= 0 && nr < n && nc >= 0 && nc < m && vis[nr][nc] == 0){
                    q.add(new int[]{nr,nc,d+1});
                    vis[nr][nc] = 1;
                }
            }
        }
        return res;
    }
}