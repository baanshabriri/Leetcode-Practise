#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        return self.isSameTree(root.left, root.right)
    
    def isSameTree(self, p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
        
        
        
# @lc code=end

