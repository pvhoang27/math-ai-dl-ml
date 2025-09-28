import numpy as np

# Định nghĩa ma trận A và B
A = np.array([[1, 2, 3],
              [-4, -4, -4],
              [5, 6, 7]])

B = np.array([[2, -5, 1],
              [0, 3, -2],
              [1, 2, -4]])

# Tính AB và BA
AB = np.dot(A, B)
BA = np.dot(B, A)

# Hàm in ma trận đẹp
def print_matrix(name, M):
    print(f"{name} =")
    for row in M:
        print(" ", row)

# In kết quả
print_matrix("AB", AB)
print()
print_matrix("BA", BA)
