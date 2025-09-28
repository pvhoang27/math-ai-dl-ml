from math import comb

# Hộp có 5 bi đỏ, 7 bi xanh. Lấy ngẫu nhiên 3 bi.
# Xác suất lấy được đúng 2 đỏ và 1 xanh?
def hypergeo(red=5, blue=7, k_red=2, k_blue=1, n=3):
    total = comb(red+blue, n)
    favorable = comb(red, k_red) * comb(blue, k_blue)
    return favorable / total

print("Xác suất 2 đỏ, 1 xanh:", hypergeo())
