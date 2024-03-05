#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        if not root:
            return []
        
        answer = []
        
        stack = deque()
        stack.append(root)


        while stack:
            level_size = len(stack)

            if level_size > 0:
                avg = round(sum(node.val for node in stack) / level_size, 5)
                answer.append(avg)

            while level_size > 0:
                node = stack.popleft()

                if node.left is not None:
                    stack.append(node.left)
                
                if node.right is not None:
                    stack.append(node.right)

                level_size -= 1

        return answer

            

        
# @lc code=end

