"""
Binary Heap. A min heap is a complete binary tree where each node is smaller
its childen. The root, therefore, is the minimum element in the tree. The min
heap use array to represent the data and operation. For example a min heap:

     4
   /   \
  50    7
 / \   /
55 90 87

Heap [0, 4, 50, 7, 55, 90, 87]

Method in class: insert, remove_min
For example insert(2) in a min heap:

     4                     4                     2
   /   \                 /   \                 /   \
  50    7      -->     50     2       -->     50    4
 / \   /  \           /  \   / \             /  \  /  \
55 90 87   2         55  90 87  7           55  90 87  7

For example remove_min() in a min heap:

     4                     87                    7
   /   \                 /   \                 /   \
  50    7      -->     50     7       -->     50    87
 / \   /              /  \                   /  \
55 90 87             55  90                 55  90

"""

"""
williamfzc:

堆特性：父节点的键值总是保持固定的序关系于任何一个子节点的键值
二叉堆：是专门为取出最大或最小节点而设计的数据结构，这种数据结构在查找一般元素方面性能和一般数组是没有多大区别的
例子是一个最小二叉堆
一般是用数组形式来储存的，节点 1 对应的子节点的位置是 2 * 1 与 2 * 1 + 1 ，节点 n 对应的子节点的位置是 2 * n 与 2 * n + 1
"""
from abc import ABCMeta, abstractmethod


class AbstractHeap(metaclass=ABCMeta):
    """Abstract Class for Binary Heap."""

    def __init__(self):
        pass

    @abstractmethod
    def perc_up(self, i):
        pass

    @abstractmethod
    def insert(self, val):
        pass

    @abstractmethod
    def perc_down(self, i):
        pass

    @abstractmethod
    def min_child(self, i):
        pass

    @abstractmethod
    def remove_min(self, i):
        pass


class BinaryHeap(AbstractHeap):
    def __init__(self):
        self.currentSize = 0
        self.heap = [(0)]

    def perc_up(self, i):
        # williamfzc 上浮节点i
        while i // 2 > 0:
            # williamfzc: i // 2 是找到他的父节点
            if self.heap[i] < self.heap[i // 2]:
                # Swap value of child with value of its parent
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    """
        Method insert always start by inserting the element at the bottom.
        it inserts rightmost spot so as to maintain the complete tree property
        Then, it fix the tree by swapping the new element with its parent,
        until it finds an appropriate spot for the element. It essentially
        perc_up the minimum element
        Complexity: O(logN)
    """

    """
    williamfzc
    
    在插入新节点时，总是从最后插入，再利用上浮方法使其融入到合适的位置
    """
    def insert(self, val):
        self.heap.append(val)
        self.currentSize = self.currentSize + 1
        self.perc_up(self.currentSize)

    """
        Method min_child returns index of smaller 2 childs of its parent
    """

    """
    williamfzc
    
    获取节点 i 的最小子节点（两个节点中比较小的一个）
    """

    def min_child(self, i):
        if 2 * i + 1 > self.currentSize:  # No right child
            return 2 * i
        else:
            # left child > right child
            if self.heap[2 * i] > self.heap[2 * i + 1]:
                return 2 * i + 1
            else:
                return 2 * i

    def perc_down(self, i):
        while 2 * i < self.currentSize:
            min_child = self.min_child(i)
            if self.heap[min_child] < self.heap[i]:
                # Swap min child with parent
                self.heap[min_child], self.heap[i] = self.heap[i], self.heap[min_child]
            i = min_child

    """
        Remove Min method removes the minimum element and swap it with the last
        element in the heap( the bottommost, rightmost element). Then, it
        perc_down this element, swapping it with one of its children until the
        min heap property is restored
        Complexity: O(logN)
    """

    """
    williamfzc
    
    插入与移除刚好是反的
    
    - 最小堆的最小值即为堆顶
    - 移除后，将最后一个元素挪到堆顶
    - 对堆顶进行下沉操作，使其到达合适的位置
    """

    def remove_min(self):
        ret = self.heap[1]  # the smallest value at beginning
        self.heap[1] = self.heap[self.currentSize]  # Repalce it by the last value
        self.currentSize = self.currentSize - 1
        self.heap.pop()
        self.perc_down(1)
        return ret
