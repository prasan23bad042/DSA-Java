class Solution {
    public boolean dfs(int[][]graph,int colors[],int v,int  c){
        colors[v] = c;
        for(int neighbor:graph[v]){
            if(colors[neighbor] == -1){
                if(dfs(graph,colors,neighbor,1-c) == false) return false;
            }
            else if(colors[neighbor] == c) return false;
        }
        return true;
    }
    public boolean isBipartite(int[][] graph) {
        int V = graph.length;
        int m = graph[0].length;       
        int [] colors = new int[V];
        Arrays.fill(colors,-1);
        for(int i=0;i<V;i++){
            if(colors[i] == -1){
                if(dfs(graph,colors,i,0) == false){
                    return false;
                }
            }
        }
        return true;
    }
}