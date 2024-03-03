#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def createLinkedList(self, arr):
        head = ListNode(arr[0])
        temp = head
        for i in range(1, len(arr)):
            new = ListNode(arr[i])
            temp.next = new
            temp = new
        return head
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        dummy = ListNode(0, head)
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            temp = cur.next
            cur.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next



x = Solution()
head = x.createLinkedList([1,2,3,4,5])
x.reverseBetween(head, 2, 4)


        

# @lc code=end

