#
# @lc app=leetcode id=719 lang=python3
#
# [719] Find K-th Smallest Pair Distance
#

# @lc code=start
from typing import List
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:

        nums.sort()        
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]

        def enough(distance):
            # slow fast pointer
            count = slow = fast = 0
            while fast < n or slow < n:
                while fast < n and nums[fast] - nums[slow] <= distance:
                    fast += 1
                
                count += fast - slow - 1 # count pairs
                slow += 1

            return count >= k


        while left < right:
            mid = left + (right - left) // 2

            if enough(mid):
                right = mid
            else:
                left = mid + 1

        return left
        

x = Solution()
print(x.smallestDistancePair([62,100,4], 2))
# @lc code=end

