# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, y=None):
        self.val = x
        self.next = y


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        pre = None
        cur = head

        while cur:
            cur.next, cur, pre = pre, cur.next, cur
        return pre


#
e = ListNode(5)
d = ListNode(4, e)
c = ListNode(3, d)
b = ListNode(2, c)
a = ListNode(1, b)

reverse_list = Solution().reverseList(a)
print(reverse_list)
# a, b = 0, 1
#
# a, b = 7, a + 0
#
# print(a, b)
# a, b = 0, 1
#
# a = 7
# b = a + 0
# print(a, b)
