#
# @lc app=leetcode id=1283 lang=python3
#
# [1283] Find the Smallest Divisor Given a Threshold
#

# @lc code=start
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        left, right = 1, max(nums)

        def condition(divisor):
            return sum((num - 1) // divisor + 1 for num in nums) <= threshold
        

        while left < right:
            mid = left + (right - left) // 2

            if condition(divisor=mid):
                right = mid
            else:
                left = mid + 1

        return left
# @lc code=end

