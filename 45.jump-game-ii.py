#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        reach, last, count = 0, 0, 0
        for i in range(len(nums) - 1):

            reach = max(reach, i + nums[i])
            if i == last:
                last = reach

                count += 1

        return count
        

x = Solution()
x.jump([2,3,1,1,4])
# @lc code=end

