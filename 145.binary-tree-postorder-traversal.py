#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def create_tree(self, arr, index):
        if index < len(arr) and arr[index] is not None:
            root = TreeNode(arr[index])
            root.left = self.create_tree(arr, 2 * index + 1)
            root.right = self.create_tree(arr, 2 * index + 2)

            return root
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res = []
        stack1 = [root]
        stack2 = []
        node = root
        while stack1:
            node = stack1.pop()
            stack2.append(node)

            if node.left is not None:
                stack1.append(node.left)

            if node.right is not None:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            res.append(node.val)

        return res

x = Solution()
root = x.create_tree([1,2,3,4,5,6,7], 0)
print(x.postorderTraversal(root))


# @lc code=end

