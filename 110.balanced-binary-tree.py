#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def create_tree(self, arr, index):
        if index < len(arr):
            if arr[index] is None:
                return None
            
            root = TreeNode(arr[index])
            root.left = self.create_tree(arr, 2 * index + 1)
            root.right = self.create_tree(arr, 2 * index + 2)
            return root
        

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.height(root) != -1
    
    def height(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return 0
        
        left = self.height(root.left)
        right = self.height(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1 
        
        return max(left, right) + 1 #actual height of the tree
        
                
# @lc code=end

