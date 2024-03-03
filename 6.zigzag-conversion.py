#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s
        
        rows = [''] * numRows
        flag = 1
        row = 0

        for char in s:

            rows[row] += char

            if row == 0:
                flag = 1
            elif row == numRows - 1:
                flag = -1

            row += flag

        return ''.join(rows)
        
# @lc code=end

