class Solution {
    public boolean dfs(ArrayList<ArrayList<Integer>>adj,boolean vis[],int v,int parent){
        vis[v] = true;
        for(Integer x:adj.get(v)){
            if(!vis[x]){
                if(dfs(adj,vis,x,v)) return true;
            }
            else if(x != parent) return true;
        }
        return false;
    }
    public boolean isCycle(int V, int[][] edges) {
        ArrayList<ArrayList<Integer>>adj = new ArrayList<>();
        for(int i=0;i<V;i++)
        {
            adj.add(new ArrayList<>());
        }
        
        for(int[]edge:edges)
        {
            adj.get(edge[0]).add(edge[1]);
            adj.get(edge[1]).add(edge[0]);
        }
        
        boolean []vis = new boolean[V];
        
        for(int i=0;i<V;i++)
        {
            if(!vis[i] && (dfs(adj,vis,i,-1))) return true;
        }
        return false;
        
    }
}