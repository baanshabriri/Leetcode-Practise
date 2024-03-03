#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
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
    
    def getValues(self, val1, val2, carry):
        sum_values = val1 + val2 + carry
        # curr_val = sum_values % 10 if sum_values > 9 else sum_values
        # carry = sum_values // 10 if sum_values > 9 else 0

        if sum_values > 9:
            curr_val = sum_values % 10
            carry = sum_values // 10
        else:
            curr_val = sum_values
            carry = 0

        return curr_val, carry

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        temp = dummy
        carry = 0
        while l1 or l2:            

            curr_val, carry = self.getValues(l1.val if l1 else 0, l2.val if l2 else 0, carry)
            
            new = ListNode(curr_val)
            temp.next = new
            temp = new

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            new = ListNode(carry)
            temp.next = new



        return dummy.next



x = Solution()
l1 = x.createLinkedList([9,9,9,9,9,9,9])
l2 = x.createLinkedList([9,9,9,9])

# print(x.addTwoNumbers(l1, l2))

        
# @lc code=end

