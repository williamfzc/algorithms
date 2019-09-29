"""
    Given a linked list, find the first node of a cycle in it.
    1 -> 2 -> 3 -> 4 -> 5 -> 1  => 1
    A -> B -> C -> D -> E -> C  => C

    Note: The solution is a direct implementation
          Floyd's cycle-finding algorithm (Floyd's Tortoise and Hare).
"""
import unittest


class Node:

    def __init__(self, x):
        self.val = x
        self.next = None


def first_cyclic_node(head):
    """
    :type head: Node
    :rtype: Node
    """
    """
    williamfzc: 
    
    重点在于差速迭代，同时有一快一慢两个迭代器
    当他们相遇，说明存在环
    """
    runner = walker = head
    while runner and runner.next:
        runner = runner.next.next
        walker = walker.next
        if runner is walker:
            break

    if runner is None or runner.next is None:
        return None

    """
    williamfzc:
    
    求环长度：
        判断出存在环时，显然快慢迭代器位于同一节点
        显然，让快节点不动，让慢节点继续走。他们相遇时，这就是环的长度
    
    求环起始点：
        当他们相遇时，快迭代器比慢迭代器多走了 环长度*n
    
        首先假设第一次相遇的时候慢指针走过的节点个数为i，设链表头部到环的起点的长度为m，环的长度为n，相遇的位置与起点与起点位置距离为k。
        于是有：
        i = m + a * n + k
        其中a为慢指针走的圈数。
    
        因为快指针的速度是慢指针的2倍，于是又可以得到另一个式子：
        2 * i = m + b * n + k
        其中b为快指针走的圈数。
    
        两式相减得：
        i = ( b - a ) * n
        也就是说i是圈长的整数倍。
    
        这是将其中一个节点放在起点，然后同时向前走m步时，此时从头部走的指针在m位置。
        而从相遇位置开始走的指针应该在距离起点i+m，i为圈长整数倍，则该指针也应该在距离起点为m的位置，即环的起点。
    """
    walker = head
    while runner is not walker:
        runner, walker = runner.next, walker.next
    return runner


class TestSuite(unittest.TestCase):

    def test_first_cyclic_node(self):

        # create linked list => A -> B -> C -> D -> E -> C
        head = Node('A')
        head.next = Node('B')
        curr = head.next

        cyclic_node = Node('C')
        curr.next = cyclic_node

        curr = curr.next
        curr.next = Node('D')
        curr = curr.next
        curr.next = Node('E')
        curr = curr.next
        curr.next = cyclic_node

        self.assertEqual('C', first_cyclic_node(head).val)


if __name__ == '__main__':

    unittest.main()
