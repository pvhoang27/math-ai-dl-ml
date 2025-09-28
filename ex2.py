import numpy as np

# Các giá trị có thể của X và Y
x = np.array([-1, 0, 1])
px = np.array([10/24, 7/24, 7/24])  # Xác suất của X
y = np.array([-1, 1])
py = np.array([0.5, 0.5])           # Xác suất của Y

# Tạo ma trận tích XY
xy = x[:, None] * y[None, :]

# Ma trận xác suất chung (giả sử X và Y độc lập)
pxy = px[:, None] * py[None, :]

print("Bảng xác suất p(x,y):")
print(pxy)

# Tính kỳ vọng E[XY]
mean_xy = np.sum(xy * pxy)

print("Giá trị kỳ vọng E[XY] =", mean_xy)
