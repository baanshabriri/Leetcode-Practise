#
# @lc app=leetcode id=1201 lang=python3
#
# [1201] Ugly Number III
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        left, right = 1, 10 ** 9
        ab = a * b
        ac = a * c
        bc = b * c
        abc = a * bc

        def enough(num):
            total = (num // a) + (num // b) + (num // c) - (num // ab) - (num // ac) - (num // bc) + (num // abc)
            return total >= n
        
        while left < right:
            mid = left + (right - left) // 2
            if enough(mid):
                right = mid
            else:
                left = mid + 1

        return left
    
# x = Solution()
# x.nthUglyNumber(n = 3, a = 2, b = 3, c = 5)
        
# @lc code=end

