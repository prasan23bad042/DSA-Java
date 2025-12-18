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
    public boolean isValid(TreeNode root,long x,long y){
        if(root == null) return true;
        if(!(root.val > x && root.val < y)) return false;
        return isValid(root.left,x,root.val) && isValid(root.right,root.val,y); 

        // one line statement
        // return root == null || (root.val > x && root.val < y) && isValid(root.left,x,root.val) && isValid(root.right,root.val,y);
    }
    public boolean isValidBST(TreeNode root) {
        return isValid(root,Long.MIN_VALUE,Long.MAX_VALUE);
    }
}