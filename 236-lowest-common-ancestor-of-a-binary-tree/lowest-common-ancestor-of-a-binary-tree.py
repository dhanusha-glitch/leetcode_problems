class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(node):
            # Base case: null node
            if not node:
                return None
            
            # If the current node is either p or q, return it
            if node == p or node == q:
                return node
            
            # Recur for left and right children
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If both left and right return a non-null value, current node is LCA
            if left and right:
                return node
            
            # Otherwise, return the non-null child (or null if both are null)
            return left if left else right
        
        # Start the DFS from the root
        return dfs(root)