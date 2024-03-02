#
# @lc app=leetcode id=668 lang=python3
#
# [668] Kth Smallest Number in Multiplication Table
#

# @lc code=start
from typing import List
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        def enough(num):
            count = 0

            for val in range(1, m+1):
                add = min(num // val, n)
                if add == 0:
                    break
                count += add
            
            return count >= k



        left, right = 1, m*n
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1

        return left

x = Solution()
x.findKthNumber(m = 3, n = 3, k = 5)

        
# @lc code=end

