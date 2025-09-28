from math import erf, sqrt

# Hàm tính P(a <= X <= b), X ~ N(mu, sigma^2)
def normal_prob(a, b, mu=0, sigma=1):
    def cdf(x):
        return (1 + erf((x-mu)/(sigma*sqrt(2))))/2
    return cdf(b) - cdf(a)

print("P(0 <= X <= 1), X~N(0,1):", normal_prob(0,1))
