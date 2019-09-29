"""
Given a linked list, swap every two adjacent nodes
and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list,
only nodes itself can be changed.
"""


class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head):
    if not head:
        return head
    start = Node(0)
    start.next = head
    current = start
    while current.next and current.next.next:
        # williamfzc: 获取第一个与第二个
        first = current.next
        second = current.next.next
        # williamfzc: 第一个元素直接指向这一对的后一个元素
        first.next = second.next
        # williamfzc: 第二个元素放到前面
        current.next = second
        # williamfzc: 第一个元素放到后面
        current.next.next = first
        # williamfzc: 这两个处理完了，指针后移，进行后面的迭代
        current = current.next.next
    return start.next
