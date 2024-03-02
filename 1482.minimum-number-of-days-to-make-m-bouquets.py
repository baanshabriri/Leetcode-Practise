#
# @lc app=leetcode id=1482 lang=python3
#
# [1482] Minimum Number of Days to Make m Bouquets
#

# @lc code=start
from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        
        left, right = 1, max(bloomDay)

        if m * k > len(bloomDay):
            return -1 


        def feasible(days) -> bool:
            bouquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bouquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k

            return bouquets >=m


        while left < right:
            mid = left + (right - left) // 2

            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
    
x = Solution()
x.minDays(bloomDay = [1,10,3,10,2], m = 3, k = 1)
# @lc code=end

