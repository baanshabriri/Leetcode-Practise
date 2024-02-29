#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
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
        if index < len(arr) and arr[index] is not None:
            root = TreeNode(arr[index])
            root.left = self.create_tree(arr, 2 * index + 1)
            root.right = self.create_tree(arr, 2 * index + 2)

            return root
        

    def preOrder(self, root: TreeNode, result: List) -> List[int]:
        if not root:
            return result
        else:
            result.append(root.val)
            self.preOrder(root.left, result)
            self.preOrder(root.right, result)
        

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.preOrder(root, result)
        return result
        # if not root:
        #     return []
        
        # res = []
        # stack = [root]        
        
        # while stack:
        #     node = stack.pop()
        #     res.append(node.val)
        #     if node.right is not None:
        #         stack.append(node.right)
        #     if node.left is not None: 
        #         stack.append(node.left)

        # return res


x = Solution()
root = x.create_tree([1,None,2,3], 0)
print(x.preorderTraversal(root))

# @lc code=end

