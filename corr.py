import numpy as np

# Dữ liệu mẫu
X = [2, 4, 6, 8, 10]
Y = [1, 3, 5, 7, 9]

# ---- Cách 1: Dùng numpy.corrcoef ----
corr_matrix = np.corrcoef(X, Y)
print("Correlation matrix:\n", corr_matrix)
print("Corr(X,Y) =", corr_matrix[0, 1])

# ---- Cách 2: Tính thủ công từ covariance ----
mean_x = np.mean(X)
mean_y = np.mean(Y)

cov_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(X, Y)) / (len(X) - 1)
std_x = np.std(X, ddof=1)  # ddof=1: mẫu
std_y = np.std(Y, ddof=1)

corr_xy = cov_xy / (std_x * std_y)
print("Corr(X,Y) (manual) =", corr_xy)
