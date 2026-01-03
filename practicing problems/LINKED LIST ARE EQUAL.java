class Solution {
    public static boolean areEqual(LinkedList<Integer> ll1, LinkedList<Integer> ll2) {
        if (ll1.size() != ll2.size()) 
            return false;
        for (int i = 0; i < ll1.size(); i++) {
            if (!ll1.get(i).equals(ll2.get(i))) {
                return false;
            }
        }
        return true;
    }
}
