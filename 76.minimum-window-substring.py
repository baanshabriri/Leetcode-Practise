#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = end = 0
        hash_map = {}
        counter = len(t)
        min_start = 0
        min_substr_len = float('inf')
        for char in t:
            hash_map[char] = hash_map.get(char, 0) + 1

        while end < len(s):
            if s[end] in hash_map:
                if hash_map[s[end]] > 0:
                    counter -= 1
                hash_map[s[end]] -= 1

            while counter == 0:
                if end - start + 1 < min_substr_len:
                    min_substr_len = end - start + 1
                    min_start = start

                if s[start] in hash_map:
                    hash_map[s[start]] += 1
                    if hash_map[s[start]] > 0:
                        counter += 1

                start += 1

            end += 1

        return '' if min_substr_len == float('inf') else s[min_start: min_start+min_substr_len]

                


x = Solution()
print(x.minWindow('ADOBECODEBANC', 'ABC'))
        
# @lc code=end

