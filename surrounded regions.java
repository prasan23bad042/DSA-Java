class Solution {
    public void solve(char[][] board) {
        int n = board.length;
        int m = board[0].length;
        Queue<int[]> q = new LinkedList<>();
        for(int j=0;j<m;j++){
            if(board[0][j] == 'O'){
                q.add(new int[]{0,j});
                board[0][j] = 'Y';
            }
            if(board[n-1][j] == 'O'){
                q.add(new int[]{n-1,j});
                board[n-1][j] = 'Y';
            }
        }
        for(int i=0;i<n;i++){
            if(board[i][0] == 'O'){
                q.add(new int[]{i,0});
                board[i][0] = 'Y';
            }
            if(board[i][m-1] == 'O'){
                q.add(new int[]{i,m-1});
                board[i][m-1] = 'Y';
            }
        }
        int row_x[] = {-1,0,1,0};
        int col_x[] = {0,-1,0,1};
        while(!q.isEmpty()){
            int x[] = q.poll();
            int i = x[0];
            int j = x[1];
            for(int k=0;k<4;k++){
                int nr = i + row_x[k];
                int nc = j + col_x[k];
                if(nr >= 0 && nr < n && nc >= 0 && nc < m && board[nr][nc] == 'O'){
                    q.add(new int[]{nr,nc});
                    board[nr][nc] = 'Y';
                }
            }
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(board[i][j] == 'Y'){
                    board[i][j] = 'O';
                }
                else if(board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
            }
        }
    }
}