#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        left = 0        
        char_map = {}
        max_freq = 0
        for right in range(len(s)):            
            char_map[s[right]] = char_map.get(s[right], 0) + 1
            max_freq = max(max_freq, char_map[s[right]])
            if right - left + 1 - max_freq > k:
                char_map[s[left]] -= 1                
                left += 1
        return right - left + 1
    

            
            
x = Solution()
print(x.characterReplacement(s='AABABBAAKBFAHBBABABABJKFA', k=1))


        
# @lc code=end

