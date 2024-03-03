#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        if len(needle) > len(haystack):
            return -1
        
        i = 0

        while i <= len(haystack) - len(needle):
            j = 0

            while j < len(needle) and haystack[i + j] == needle[j]:
                j += 1

                if j == len(needle):
                    return i
                
            i += 1

        return -1 


# @lc code=end

