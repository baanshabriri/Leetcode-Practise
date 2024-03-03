#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        
        before, after = ListNode(-1), ListNode(-1)
        temp_before, temp_after = before, after

        curr = head
        while curr:
            if curr.val < x:
                temp_before.next = curr
                temp_before = temp_before.next

            else:
                temp_after.next = curr
                temp_after = temp_after.next

            curr = curr.next

        temp_after.next = None
        temp_before.next = after.next

        return before.next







        
# @lc code=end

