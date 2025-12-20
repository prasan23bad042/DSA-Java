class Solution {
    ArrayList<ArrayList<Integer>> ans = new ArrayList<>();
    public void bfs(ArrayList<ArrayList<Integer>> adj,int v,boolean[]vis){
        ArrayList<Integer> temp = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        q.add(v);
        temp.add(v);
        vis[v] = true;
        while(!q.isEmpty()){
            int x = q.poll();
            for(int y:adj.get(x)){
                if(!vis[y]){
                    q.add(y);
                    vis[y] = true;
                    temp.add(y);
                }
            }
        }
        ans.add(temp);
    }
    public ArrayList<ArrayList<Integer>> getComponents(int V, int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=1;i<=V;i++){
            adj.add(new ArrayList<>());
        }
        for(int[] edge:edges){
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        boolean [] vis = new boolean[V];
        for(int i=0;i<V;i++){
            if(!vis[i]){
                bfs(adj,i,vis);
            }
        }
        return ans;
    }
}