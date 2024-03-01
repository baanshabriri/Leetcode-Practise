#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answers = []

        subset = []

        def dfs(index):
            if index >= len(nums):
                answers.append(subset.copy())
                return
            
            subset.append(nums[index])

            dfs(index + 1)

            subset.pop()

            dfs(index + 1)

        dfs(0)

        return answers


x = Solution()
x.subsets([1,2,3])
        
# @lc code=end

