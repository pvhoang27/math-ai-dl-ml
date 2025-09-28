import random

# Tung đồng xu 10 lần, xác suất được 5 lần ngửa
def coin_binomial(n=10, p=0.5, k=5):
    from math import comb
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

print("Xác suất được đúng 5 lần ngửa:", coin_binomial())
