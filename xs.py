# Xác suất tổng 2 viên xúc xắc bằng 7
def dice_sum_7():
    count = 0
    for i in range(1,7):
        for j in range(1,7):
            if i + j == 7:
                count += 1
    return count / 36

print("Xác suất tổng = 7:", dice_sum_7())
