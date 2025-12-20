class Solution {
    public void bfs(int[][]isConnected,boolean [] visited,int v){
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        visited[v] = true;
        while(!q.isEmpty()){
            int x = q.poll();
            for(int i=0;i<isConnected.length;i++){
                if(isConnected[x][i] == 1 && !visited[i]){
                    q.add(i);
                    visited[i] = true;
                }
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int v = isConnected.length;
        boolean []visited = new boolean[v];
        int provinces = 0;
        for(int i=0;i<v;i++){
            if(!visited[i]){
                provinces++;
                bfs(isConnected,visited,i);
            }
        }
        return provinces;
    }
}