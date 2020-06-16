# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1.next!=None or l2.next!=None:
            result= ListNode(l1.val+l2.val)
            result.next=addTwoNumbers(l1.next, l2.next)
            return result
        return ListNode(l1.val+l2.val)