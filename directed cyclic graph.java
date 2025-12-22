import java.util.*;

class Solution {
    public boolean dfs(int u, ArrayList<ArrayList<Integer>> adj,
                       int[] vis, int[] pathVis) {
        vis[u] = 1;
        pathVis[u] = 1;
        for (int v : adj.get(u)) {
            if (vis[v] == 0) {
                if (dfs(v, adj, vis, pathVis))
                    return true;
            }
            else if (pathVis[v] == 1) {
                return true;   
            }
        }
        pathVis[u] = 0;   
        return false;
    }
    public boolean isCyclic(int V, int[][] edges) {

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < V; i++)
            adj.add(new ArrayList<>());

        for (int[] e : edges) {
            adj.get(e[0]).add(e[1]);
        }
        int[] vis = new int[V];
        int[] pathVis = new int[V];

        for (int i = 0; i < V; i++) {
            if (vis[i] == 0) {
                if (dfs(i, adj, vis, pathVis))
                    return true;
            }
        }
        return false;
    }
}
