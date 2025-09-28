import numpy as np

# --- Ma trận a) ---
A1 = np.array([[1, 3], 
               [0, 1]])

# --- Ma trận b) ---
# Sử dụng dtype=object để xử lý các số rất lớn mà không bị tràn (overflow)
A2 = np.array([[2, 3], 
               [0, 2]], dtype=object)

# --- Ma trận c) ---
# Tương tự, sử dụng dtype=object
A3 = np.array([[1, 1], 
               [1, 1]], dtype=object)

# Tính A^200 cho mỗi ma trận bằng hàm numpy.linalg.matrix_power
A1_200 = np.linalg.matrix_power(A1, 200)
A2_200 = np.linalg.matrix_power(A2, 200)
A3_200 = np.linalg.matrix_power(A3, 200)

# In kết quả
print("### Kết quả cho ma trận a) ###")
print(f"A = \n{A1}")
print(f"A^200 = \n{A1_200}\n")
# Kết quả này khớp với [[1, 600], [0, 1]]

print("### Kết quả cho ma trận b) ###")
print(f"A = \n{A2}")
print(f"A^200 = \n{A2_200}\n")
# Phần tử [0, 0] và [1, 1] là 2^200
# Phần tử [0, 1] là 600 * 2^199

print("### Kết quả cho ma trận c) ###")
print(f"A = \n{A3}")
print(f"A^200 = \n{A3_200}\n")
# Tất cả các phần tử đều là 2^199