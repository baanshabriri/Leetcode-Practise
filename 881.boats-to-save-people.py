#
# @lc app=leetcode id=881 lang=python3
#
# [881] Boats to Save People
#

# @lc code=start
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start = 0
        end = len(people) - 1
        boat_count = 0
        while start <= end:
            if people[start] + people[end] <= limit:                
                start += 1                
            end -= 1
            boat_count += 1

        return boat_count
    
x = Solution()
x.numRescueBoats([3,5,3,4], 5)



# @lc code=end

