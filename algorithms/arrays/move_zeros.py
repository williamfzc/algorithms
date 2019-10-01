"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""

"""
williamfzc

将列表中的 0 移动到 末尾，两种思路：

- 找0，移动到末尾
- 找非0，移动到头部
"""
# False == 0 is True
def move_zeros(array):
    result = []
    zeros = 0

    for i in array:
            if i == 0 and type(i) != bool:  # not using `not i` to avoid `False`, `[]`, etc.
                zeros += 1
            else:
                result.append(i)
    
    result.extend([0] * zeros)
    return result


print(move_zeros([False, 1, 0, 1, 2, 0, 1, 3, "a"]))