import numpy as np

# Dữ liệu mẫu
X = [2, 4, 6, 8, 10]
Y = [1, 3, 5, 7, 9]

# ---- Cách 1: Dùng numpy.cov ----
cov_matrix = np.cov(X, Y, bias=False)  # bias=False: mẫu (sample covariance)
print("Covariance matrix:\n", cov_matrix)
print("Cov(X,Y) =", cov_matrix[0, 1])

# ---- Cách 2: Tính thủ công ----
mean_x = np.mean(X)
mean_y = np.mean(Y)

cov_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y)) / (len(X) - 1)
print("Cov(X,Y) (manual) =", cov_xy)
