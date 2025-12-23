class Solution {
    public ArrayList<Integer> topoSort(int V, int[][] edges) {
        int [] in = new int[V];
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
        }
        for(int[] edge:edges){
            adj.get(edge[0]).add(edge[1]);
        }
        for(int i=0;i<V;i++){
            for(int it:adj.get(i)){
                in[it]++;        
            }
        }
        ArrayList<Integer> ans = new ArrayList<>();
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<V;i++){
            if(in[i] == 0) q.add(i);
        }
        while(!q.isEmpty()){
            int x = q.poll();
            ans.add(x);
            for(int it:adj.get(x)){
                in[it]--;
                if(in[it] == 0){
                    q.add(it);
                }
            }
        }
        return ans;
    }
}