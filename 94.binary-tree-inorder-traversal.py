#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional
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

    def inOrder(self, node, result):
        if not node:
            return result
        else:
            self.inOrder(node.left, result)
            result.append(node.val)
            self.inOrder(node.right, result)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []        
        
        res = []

        self.inOrder(root, res)
        return res
        # stack = []
        # node = root

        # while node or stack:
        #     while node:
        #         stack.append(node)
        #         node = node.left

        #     node = stack.pop()
        #     res.append(node.val)
        #     node = node.right
        
        # return res



# @lc code=end

