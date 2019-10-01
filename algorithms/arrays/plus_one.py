"""
Given a non-negative number represented as an array of digits,
adding one to each numeral.

The digits are stored big-endian, such that the most significant
digit is at the head of the list.
"""

"""
williamfzc

将数字以list形式保存，每一位对应一个数字。实现 +1 的运算。
核心就是考察对进位的处理：

- 不满足10，加完退出
- 超过10，取余数，继续找上一位
- 最后一位如果为0，需要在前面加上1
"""

def plus_one_v1(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    digits[-1] = digits[-1] + 1
    res = []
    ten = 0
    i = len(digits)-1
    while i >= 0 or ten == 1:
        summ = 0
        if i >= 0:
            summ += digits[i]
        if ten:
            summ += 1
        res.append(summ % 10)
        ten = summ // 10
        i -= 1
    return res[::-1]


def plus_one_v2(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    digits.insert(0, 1)
    return digits


def plus_one_v3(num_arr):

    for idx in reversed(list(enumerate(num_arr))):
        num_arr[idx[0]] = (num_arr[idx[0]] + 1) % 10
        if num_arr[idx[0]]:
            return num_arr
    return [1] + num_arr
