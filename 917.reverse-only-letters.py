#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        s_arr = list(s)
        while left <= right:
            if not str(s_arr[left]).isalpha():
                left += 1
            elif not str(s_arr[right]).isalpha():
                right -= 1
            else:
                s_arr[left], s_arr[right] = s_arr[right], s_arr[left]
                left += 1
                right -= 1


        return ''.join(s_arr)
            
# @lc code=end

