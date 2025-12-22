// User function Template for Java

class Solution {
    
    String bfs(int[][] grid,int sr,int sc){
        StringBuilder res = new StringBuilder();
        Queue<int[]> q = new LinkedList<>();
        int n = grid.length;
        int m = grid[0].length;
        q.add(new int[]{sr,sc});
        grid[sr][sc] = 0;
        res.append("0 0");
        int row_x[] = {-1,0,1,0};
        int col_x[] = {0,-1,0,1};
        while(!q.isEmpty()){
            int [] x = q.poll();
            int i = x[0];
            int j = x[1];
            for(int k=0;k<4;k++){
                int nr = i+row_x[k];
                int nc = j+col_x[k];
                if(nr >= 0 && nr < n && nc >= 0 && nc < m && grid[nr][nc] == 1){
                    q.add(new int[]{nr,nc});
                    grid[nr][nc] = 0;
                    res.append(Integer.toString(nr-sr) + " " + Integer.toString(nc-sc));
                }
            }
        }
        return res.toString();
    } 
    int countDistinctIslands(int[][] grid) {
        Queue<int[]> q = new LinkedList<>();
        int n = grid.length;
        int m = grid[0].length;
        HashSet<String> islands = new HashSet<>();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j] == 1){
                    islands.add(bfs(grid,i,j));
                }
            }
        }
        return islands.size();
    }
}
