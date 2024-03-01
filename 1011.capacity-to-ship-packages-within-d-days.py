#
# @lc app=leetcode id=1011 lang=python3
#
# [1011] Capacity To Ship Packages Within D Days
#

# @lc code=start
from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def feasible(capacity) -> bool:
            days_needed = 1
            total = 0
            for weight in weights:
                total += weight
                if total > capacity:
                    days_needed += 1
                    total = weight                    

                    if days_needed > days:
                        return False 
                    
            return True
        

        left, right = max(weights), sum(weights)
        while left < right:
            mid = left + (right - left) // 2
            
            if feasible(mid):
                right = mid

            else:
                left = mid + 1

        return left


x = Solution()
print(x.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))

        
# @lc code=end

