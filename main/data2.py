class ListNode:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or n < m:
            return head

        cur = head
        end = cur
        prev = None
        next = None
        start = cur
        for i in range(m, 1):
            start = cur
            cur = cur.next
            end = cur
        for i in range(m, n):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        start.next = prev
        end.next = cur
        if (m == 1):
            return prev

        return head


if __name__ == '__main__':

    for i in range( 7,10):
        print(i)
    # Solution().reverseBetween(8, 2, 3)
