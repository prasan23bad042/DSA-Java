class Solution {
    public boolean isCyclic(int V, int[][] edges) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
        }
        for(int [] edge:edges){
            adj.get(edge[0]).add(edge[1]);
        }
        int []in = new int[V];
        int c = 0;
        for(int i=0;i<V;i++){
            for(int it:adj.get(i)){
                in[it]++;
            }
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<V;i++){
            if(in[i] == 0){
                q.add(i);
            }
        }
        while(!q.isEmpty()){
            int x = q.poll();
            c++;
            for(int it:adj.get(x)){
                in[it]--;
                if(in[it] == 0){
                    q.add(it);
                }
            }
        }
        return c != V;
    }
}