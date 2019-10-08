"""
Given two binary strings,
return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
"""


def add_binary(a, b):
    s = ""
    c, i, j = 0, len(a)-1, len(b)-1
    zero = ord('0')

    """
    williamfzc
    
    c == 1 的意义在于，当两个列表都遍历完成时，检测进位是否存在。如存在，则还需要继续进位
    """
    while i >= 0 or j >= 0 or c == 1:
        """
        williamfzc
        
        这种写法已经带了自动补位（补0），用其他写法时需要考虑
        原因是，当字符串长度不相等时，需要特别处理
        """
        if i >= 0:
            c += ord(a[i]) - zero
            i -= 1
        if j >= 0:
            c += ord(b[j]) - zero
            j -= 1
        s = chr(c % 2 + zero) + s

        """
        williamfzc
        
        计算进位：
        0 // 2 = 0
        1 // 2 = 0
        2 // 2 = 1
        """
        c //= 2

    return s
