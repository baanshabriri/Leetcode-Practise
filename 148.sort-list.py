#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def create_linked_list(self, arr):
        if not arr:
            return None
        
        head = ListNode(arr[0])
        current = head
        
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return head

    def merge(self, a: Optional[ListNode],  b: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0)
        temp = dummy

        left = a
        right = b
        
        while left != None and right != None:
            if left.val < right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            
            temp = temp.next

        if left:
            temp.next = left
            temp = temp.next
            left = left.next
        
        if right:
            temp.next = right
            temp = temp.next
            right = right.next

        return dummy.next


    def findMid(self, head):
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow
    
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        left = head
        mid = self.findMid(head) 
        right = mid.next
        mid.next = None

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

        

# @lc code=end

