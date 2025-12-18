/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    int c;
    int ans;
    public void inOrder(TreeNode root,int k){
        if(root != null){
            System.out.println(root.val);
            inOrder(root.left,k);
            c += 1;
            if(c == k){
                ans = root.val;
                return;
            }
            inOrder(root.right,k);
        }
    }
    public int kthSmallest(TreeNode root, int k) {
        inOrder(root,k);
        return ans;
    }
}   