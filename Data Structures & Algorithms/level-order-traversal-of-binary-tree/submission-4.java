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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res= new ArrayList<>();
        Deque<TreeNode> q = new ArrayDeque<>();
        if(root!=null){
            q.add(root);
        }
        else {
            return res;
        }
        while (!q.isEmpty()){
            int size=q.size();
            List<Integer> temp = new ArrayList<>();
            for(int i=0;i<size;i++){
                TreeNode node=q.poll();
                if(node!=null){
                    temp.add(node.val);
                    if(node.left!=null)q.add(node.left);
                    if(node.right!=null)q.add(node.right);
                }
            }
            res.add(temp);
        }
        return res;

    }
}
