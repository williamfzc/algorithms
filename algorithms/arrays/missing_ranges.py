"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""

"""
williamfzc

意思是在 [1, 10] 这个区间内，插入 [3, 5] 两个点的话可以将区间分为几个部分
"""
def missing_ranges(arr, lo, hi):

    res = []
    start = lo

    for n in arr:
        # williamfzc: 如果 n 即当前点，跳过该点即可
        if n == start:
            start += 1
        # williamfzc: 如果 n 比当前点领先一些，那么将 ( start, n-1 ) 即为所求区间
        elif n > start:
            res.append((start, n-1))
            # williamfzc: 在处理后，将当前点设置为 n + 1 位置
            start = n + 1

    if start <= hi:                 # after done iterating thru array,
        res.append((start, hi))     # append remainder to list

    return res
