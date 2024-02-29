#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
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
        
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        if not root:
            return []
        
        queue = deque()
        queue.append(root)

        isOddLevel = False
        while queue:            
            level = []
            level_size = len(queue)
            new_queue = deque()
            while level_size > 0:

                node = queue.popleft()
                level.append(node.val)      

                if isOddLevel:
                    if node.right is not None:
                        new_queue.appendleft(node.right)
                    if node.left is not None:
                        new_queue.appendleft(node.left)
                else:
                    if node.left is not None:
                        new_queue.appendleft(node.left)
                    if node.right is not None:
                        new_queue.appendleft(node.right)

                level_size -= 1
            
            res.append(level)
            queue = new_queue
            isOddLevel = not isOddLevel

        return res
                
# @lc code=end

