import numpy as np
# 创建数组
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
b[1, 1] = 10

# 输出结果
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)