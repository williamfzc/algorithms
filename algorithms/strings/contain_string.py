"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
Reference: https://leetcode.com/problems/implement-strstr/description/
"""
def contain_string(haystack, needle):
    # williamfzc 特殊情况
    if len(needle) == 0:
        return 0
    if len(needle) > len(haystack):
        return -1
    for i in range(len(haystack)):
        # williamfzc: 剩下的比 待比较词 短，还没找到，就直接结束
        if len(haystack) - i < len(needle):
            return -1
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1
