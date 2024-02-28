#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def reverse_linked_list(head: ListNode) -> ListNode:
            prev = forward = None
            curr = head

            while curr != None:
                forward = curr.next
                curr.next = prev
                prev = curr
                curr = forward

            return prev

        fast = head
        slow = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next


        slow = reverse_linked_list(slow)

        while slow != None and slow.val == head.val:
            slow = slow.next
            head = head.next

        return slow == None
        


        
# @lc code=end

