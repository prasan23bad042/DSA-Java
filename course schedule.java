class Solution {
    public boolean canFinish(int V, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
        }
        for(int[] edge:prerequisites){
            adj.get(edge[0]).add(edge[1]);
        }
        int in[] = new int[V];
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
        ArrayList<Integer> ans = new ArrayList<>();
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
        return ans.size() == V;
    }
}