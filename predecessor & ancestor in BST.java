/*
class Node {
    int data;
    Node left, right;
    Node(int x) {
        data = x;
        left = right = null;
    }
}
*/

class Solution {
    Node succ = null;
    Node pre = null;
    public void getSuccessor(Node root,int key){
        while(root != null){
            if(key >= root.data) root = root.right;
            else{
                if(succ != null && root.data < succ.data)
                    succ = root;
                if(succ == null) succ = root;
                root = root.left;
            }
        }
    }
    public void getPredecessor(Node root,int key){
        while(root != null){
            if(key <= root.data) root = root.left;
            else{
                if(pre != null && root.data > pre.data)
                    pre = root;
                if(pre == null) pre = root;
                root = root.right;
            }
        }
    }
    public ArrayList<Node> findPreSuc(Node root, int key) {
        ArrayList<Node> ans = new ArrayList<>();
        getPredecessor(root,key);
        getSuccessor(root,key);
        ans.add(pre);
        ans.add(succ);
        return ans;
        
    }
}