"""
Reverse a singly linked list. For example:

1 --> 2 --> 3 --> 4
After reverse:
4 --> 3 --> 2 --> 1
"""
#
# Iterative solution
# T(n)- O(n)
#
def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head or not head.next:
        return head
    prev = None
    while head:
        current = head
        # williamfzc: 将head移动到下一位
        head = head.next
        # williamfzc: 将next指向上一位（反转）
        current.next = prev
        # williamfzc: 更新 prev（因为head已经往后移动了）
        prev = current
    return prev


#
# Recursive solution
# T(n)- O(n)
#
def reverse_list_recursive(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head
    p = head.next
    head.next = None
    revrest = reverse_list_recursive(p)
    p.next = head
    return revrest
