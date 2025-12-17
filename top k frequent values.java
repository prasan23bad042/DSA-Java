class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> mp = new HashMap<>();
        for(int x:nums)
            mp.put(x,mp.getOrDefault(x,0)+1);
        PriorityQueue<int[]> pq = new PriorityQueue<>((a,b)->a[1]-b[1]);
        for(Map.Entry<Integer,Integer> m:mp.entrySet()){
            pq.add(new int[]{m.getKey(),m.getValue()});
            if(pq.size()>k)
                pq.poll();
        }
        int [] ans = new int[k];
        int i = 0;
        while(!pq.isEmpty()){
            ans[i++] = pq.poll()[0];
        }
        return ans;
    }
}