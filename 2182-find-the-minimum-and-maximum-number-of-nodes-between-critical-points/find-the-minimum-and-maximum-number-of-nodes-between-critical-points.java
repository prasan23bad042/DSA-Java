class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        int Min = 100000, i = 1;
        int first = 0, last = 0;

        ListNode prev = head, curr = head.next, nxt = head.next.next;

        while (nxt != null) {
            if (isCrit(prev, curr, nxt)) {
                if (first == 0) first = i;
                else Min = Math.min(Min, i - last);
                last = i;
            }

            prev = curr; curr = nxt;
            nxt = nxt.next; i++;
        }

        if (first == last) return new int[]{-1, -1};

        return new int[]{Min, last - first};
    }
    
    boolean isCrit(ListNode a, ListNode b, ListNode c) {
        return (a.val < b.val && b.val > c.val) ||
               (a.val > b.val && b.val < c.val);
    }
}