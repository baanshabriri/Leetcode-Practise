#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
from typing import List
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        
        def feasible(bananas_per_hour):                                                        
            return sum((pile - 1) // bananas_per_hour + 1 for pile in piles) <= h


        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else: 
                left = mid + 1

        return left
    
x = Solution()
x.minEatingSpeed([30,11,23,4,20], 5)

        
# @lc code=end

