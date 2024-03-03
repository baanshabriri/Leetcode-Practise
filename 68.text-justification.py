#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result, current_list, num_of_letters = [], [], 0

        for word in words:

            if num_of_letters + len(current_list) + len(word) > maxWidth:

                size = max(1, len(current_list) - 1)

                for i in range(maxWidth - num_of_letters):
                    index = i % size
                    current_list[index] += ' '
                
                
                result.append("".join(current_list))
                current_list, num_of_letters = [], 0

            current_list.append(word)
            num_of_letters += len(word)
        
        result.append(' '.join(current_list).ljust(maxWidth))
        return result

        

x = Solution()
x.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16)







        
# @lc code=end

