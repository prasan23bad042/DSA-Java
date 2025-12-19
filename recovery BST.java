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
    TreeNode prev = null;
    TreeNode first = null,middle = null,last = null;
    public void inOrder(TreeNode root){
        if(root != null){
            //------
            inOrder(root.left);
            if(prev != null && (root.val < prev.val)){
                if(first == null){
                    first = prev;
                    middle = root;
                }
                else{
                    last = root;
                }
            }
            prev = root;
            //------
            System.out.print(root.val);
            //-------
            inOrder(root.right);
        }
    }
    public void swap(TreeNode first,TreeNode last){
        int temp = first.val;
        first.val = last.val;
        last.val = temp;
    }
    public void recoverTree(TreeNode root) {
        inOrder(root);
        if(first != null && last != null) swap(first,last);
        else if(first != null && middle != null) swap(first,middle);
    }
}