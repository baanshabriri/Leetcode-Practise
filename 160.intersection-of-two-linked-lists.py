#
# @lc app=leetcode id=160 lang=python3
#
# [160] Intersection of Two Linked Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:


        a = headA
        b = headB
        while a!=b:
            if a != None:
                a = a.next
            else:
                a = headB

            if b != None:
                b = b.next
            else:
                b = headA
        return b


        
        
# @lc code=end

