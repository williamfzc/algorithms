"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""

"""
williamfzc

leetcode 的第一道题

这里的方法用了 dict 作为缓存（d[值] = 在列表中的位置）
值得注意，second = target - first，这个也可以用于降维 3SUM 的问题
"""
def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None
