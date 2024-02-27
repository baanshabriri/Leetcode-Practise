#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
from math import sqrt, floor
class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        start = 0
        end = floor(sqrt(c))

        while start <= end:
            square_sum = pow(start, 2) + pow(end, 2)
            if square_sum == c:
                return True
            elif square_sum < c:
                start += 1
            else:
                end -= 1


x = Solution()
x.judgeSquareSum(5)
        
# @lc code=end

