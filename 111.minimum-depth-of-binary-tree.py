#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque

class Solution:
    def create_tree(self, arr, index):
        if index < len(arr):
            if arr[index] is None:
                return None
            
            root = TreeNode(arr[index])
            root.left = self.create_tree(arr, 2 * index + 1)
            root.right = self.create_tree(arr, 2 * index + 2)
            return root
        
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        if root.left is None:
            return 1 + self.minDepth(root.right)
        
        if root.right is None:
            return 1 + self.minDepth(root.left)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
        


x = Solution()
root = x.create_tree([3,9,20,None,None,15,7], 0)
print(x.minDepth(root))


            

        
# @lc code=end

