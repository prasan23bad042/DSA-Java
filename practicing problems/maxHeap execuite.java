// User function Template for Java
class Solution {
    public static PriorityQueue<Integer> insertion(ArrayList<Integer> arr) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        for(int x: arr) pq.add(x);
        return pq;
    }
}