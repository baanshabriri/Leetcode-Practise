#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.res = set()

        def bfs(root, target):

            if not root:
                return
            
            if target - root.val in self.res: 
                return True
            
            self.res.add(root.val)
            x = bfs(root=root.left, target=k) or bfs(root=root.right, target=k)

            return x
        
        return bfs(root=root, target=k)


            
# x = Solution()            
# x.findTarget([5,3,6,2,4,None,7], 28)


        
# @lc code=end

