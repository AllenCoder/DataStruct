class ListNode:
    def __init__(self, value, next_value=None):
        self.value = value
        self.next = next_value


def reverse(pHead):
    """
    单链表翻转
    :param data:
    :return:
    """

    if pHead is None or pHead.next is None:
        return pHead
    pre = None
    while pHead:
        tmp = pHead.next
        pHead.next = pre
        pre = pHead
        pHead = tmp
    return pre


# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead is None or pHead.next is None:
            return pHead
        pre = None
        while pHead:
            tmp = pHead.next
            pHead.next = pre
            pre = pHead
            pHead = tmp
        return pHead


if __name__ == '__main__':
    head = ListNode(1)
    one = ListNode(2, next_value=head)
    two = ListNode(3, next_value=one)
    three = ListNode(4, next_value=two)
    values = reverse(three)
    print(values)
