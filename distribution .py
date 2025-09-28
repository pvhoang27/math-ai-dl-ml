import numpy as np

x = np.array([1, 2, 1])


px = np.array([0.45, 0.55])


y = np.array([1, 2, 3])

py = np.array([0.25 ,0.3, 0.45])


xy = x[:,None] * y[None, :]

print(xy)

# pxy = px[:,None] * py[None, :]

# mean_xy = sum(xy * pxy)
