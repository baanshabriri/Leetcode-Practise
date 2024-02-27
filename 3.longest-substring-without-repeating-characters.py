#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        hash_map = {}

        start = end = 0
        for end in range(len(s)):
            if s[end] not in hash_map or hash_map[s[end]] < start:                
                max_len = max(max_len, end - start + 1)
            else:
                start = hash_map[s[end]] + 1
                
            hash_map[s[end]] = end
        return max_len

                
        
        
# @lc code=end

