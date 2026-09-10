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
    int main_ans = 0;
    public int[] postOrder(TreeNode root){
        if(root == null) return new int[]{0,0};
        int[] l = postOrder(root.left);
        int[] r = postOrder(root.right);
        int sum = l[0] + r[0] + root.val;
        int c = l[1] + r[1] + 1;
        if(sum/c == root.val) main_ans += 1;
        return new int[]{sum,c};

    }
    public int averageOfSubtree(TreeNode root) {
        postOrder(root);
        return main_ans;
    }
}