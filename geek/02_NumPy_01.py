import numpy as np

arr_1_d = np.asarray([1])
print(arr_1_d)
print(arr_1_d.shape)

arr_2_d = np.asarray([[1, 2], [3, 4]])
print(arr_2_d)
print(arr_2_d.shape)

arr_2_d_rs = arr_2_d.reshape((4, 1))
print(arr_2_d_rs)
print(arr_2_d_rs.shape)

a = np.arange(6).reshape(2, 3)
print(a)
print(a.size)
print(a.dtype)

arr_2_d_dt = np.asarray([[1, 2], [3, 4]], dtype='float')
print(arr_2_d_dt.dtype)
arr_2_d_int64 = arr_2_d_dt.astype(dtype='int64')
print(arr_2_d_int64.dtype)
