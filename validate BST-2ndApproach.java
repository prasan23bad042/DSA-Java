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
    ArrayList<Integer> ans = new ArrayList<>();
    public void inOrder(TreeNode root){
        if(root != null){
            inOrder(root.left);
            ans.add(root.val);
            inOrder(root.right);
        }
    }
    public boolean isValidBST(TreeNode root) {
        inOrder(root);
        for(int i=1;i<ans.size();i++){
            if(ans.get(i) <= ans.get(i-1))
                return false;
        }
        return true;
    }
}