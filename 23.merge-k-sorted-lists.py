#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge_linked_lists(self, headA: ListNode, headB: ListNode):
            dummy = ListNode(-1)
            temp = dummy

            a = headA
            b = headB

            while a!= None and b!= None:
                if a.val < b.val:
                    temp.next = a
                    temp = temp.next
                    a = a.next
                else:
                    temp.next = b
                    temp = temp.next
                    b = b.next

            while a:
                temp.next = a
                temp = temp.next
                a = a.next

            while b:
                temp.next = b
                temp = temp.next
                b = b.next

            return dummy.next
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        return self.merge_sort(lists, 0, len(lists) - 1)

    def merge_sort(self, lists: List[Optional[ListNode]], start, end) -> ListNode:
        if start == end:
            return lists[start]
        
        mid = start + (end - start) // 2
        left = self.merge_sort(lists, start, mid)
        right = self.merge_sort(lists, mid + 1, end)

        return self.merge_linked_lists(left, right)


        
# @lc code=end

