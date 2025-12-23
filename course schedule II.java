class Solution {
    public int[] findOrder(int V, int[][] prerequisites) {
        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
        for(int i=0;i<V;i++){
            adj.add(new ArrayList<>());
        }
        int in[] = new int[V];
        for(int[] edge:prerequisites){
            adj.get(edge[1]).add(edge[0]);
            in[edge[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for(int i=0;i<V;i++){
            if(in[i] == 0){
                q.add(i);
            }
        }
        int [] ans = new int[V];
        int i = 0;
        while(!q.isEmpty()){
            int x = q.poll();
            ans[i++] = x;
            for(int it:adj.get(x)){
                in[it]--;
                if(in[it] == 0){
                    q.add(it);
                }
            }
        }
        if(i == V) return ans;
        int arr[] = {};
        return arr; 
    }
}