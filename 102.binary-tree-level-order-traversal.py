#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
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
        

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
            
        stack = deque()
        stack.append(root)
        
        while stack:
            level = []
            level_size = len(stack)
            while level_size > 0:
                node = stack.popleft()
                level.append(node.val)
                
                if node.left is not None:
                    stack.append(node.left)

                if node.right is not None:
                    stack.append(node.right)

                level_size -= 1

            res.append(level)
        
        return res
            
# @lc code=end

