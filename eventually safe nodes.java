class Solution {
    public List<Integer> eventualSafeNodes(int[][] graph) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        int V = graph.length;
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
        }
        int in[] = new int[V];
        for(int i=0;i<V;i++){
            for(int edge:graph[i]){
                adj.get(edge).add(i);
                in[i]++;
            }
        }
        
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<V;i++){
            if(in[i] == 0){
                q.add(i);
            }
        }
        List<Integer> ans = new ArrayList<>();
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
        Collections.sort(ans);
        return ans;
    }
}