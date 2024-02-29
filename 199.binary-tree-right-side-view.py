#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:

    def dfs(self, root: Optional[TreeNode], res: List, level: int) -> list:
        if not root:
            return []
        
        if len(res) == level:
            res.append(root.val)

        self.dfs(root.right, res, level + 1)
        self.dfs(root.left, res, level + 1)
        

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = deque()
        stack.append(root)

        while stack:
            
            level_size = len(stack)
            res.append(stack[0].val)
            
            while level_size > 0:                
                node = stack.popleft()
                
                if node.right is not None:
                    stack.append(node.right)
                
                if node.left is not None:
                    stack.append(node.left)

                level_size -= 1

        return res


        # DFS
        # res = []
        # self.dfs(root, res, level=0)
        # return res
        
# @lc code=end

