"""
A linked list is given such that each node contains an additional random
pointer which could point to any node in the list or null.

Return a deep copy of the list.
"""
from collections import defaultdict


class RandomListNode(object):
    # williamfzc: 带了一个随机指针，这个指针可以为空，也可以指向链表的任意一个节点
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


def copy_random_pointer_v1(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """

    """
    williamfzc:
    
    本质上是用字典来缓存所有节点。两次遍历：
    
    - 第一次建立所有节点，并建立一个源节点与新节点的 dict （可以从源节点key关联到新节点value）
    - 第二次关联指针
    """
    dic = dict()
    m = n = head
    while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
    while n:
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
    return dic.get(head)


# O(n)
def copy_random_pointer_v2(head):
    """
    :type head: RandomListNode
    :rtype: RandomListNode
    """
    copy = defaultdict(lambda: RandomListNode(0))
    copy[None] = None
    node = head
    while node:
        copy[node].label = node.label
        copy[node].next = copy[node.next]
        copy[node].random = copy[node.random]
        node = node.next
    return copy[head]
