#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:


        prev = forward = None
        curr = head

        while curr != None:
            forward = curr.next
            curr.next = prev
            prev = curr
            curr = forward
        
        return prev
        
# @lc code=end

