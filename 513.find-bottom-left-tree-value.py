#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque
from typing import Optional
class Solution:

    def create_tree(self, arr, index):
        if index > len(arr) or arr[index] is None:
            return None
            
        root = TreeNode(arr[index])
        root.left = self.create_tree(arr, 2 * index + 1)
        root.right = self.create_tree(arr, 2 * index + 2)
        return root
        

    def dfs(self, root: Optional[TreeNode], res, level) -> list:
        if not root:
            return res
        
        if len(res) == level:
            res.append(root.val)
        
        self.dfs(root.left, res, level+1)
        self.dfs(root.right, res, level+1)


    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

        res = []
        self.dfs(root, res, level=0)
        return res.pop()

        # BFS
        # if not root:
        #     return 0
        # res = []
        # queue = deque()
        # queue.append(root)

        # while len(queue) > 0:
        #     level_size = len(queue)            
        #     res.append(queue[0].val)

        #     while level_size > 0:
        #         node = queue.popleft()
        #         if node.left is not None:
        #             queue.append(node.left)

        #         if node.right is not None:
        #             queue.append(node.right)

        #         level_size -= 1
        
        # return res.pop()
    

# x = Solution()
# root = x.create_tree([1,2,3,4,None,5,6,None,None,7],0 )
# print(x.findBottomLeftValue(root))
# @lc code=end

