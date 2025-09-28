# Ước lượng pi bằng Monte Carlo
import random
def monte_carlo_pi(n=100000):
    inside = 0
    for _ in range(n):
        x, y = random.random(), random.random()
        if x*x + y*y <= 1:
            inside += 1
    return 4 * inside / n

print("Ước lượng Pi:", monte_carlo_pi())
