import math
combination = [[0 for i in range(1001)] for j in range(1001)]
def calc():
    mod = 10**9+7
    combination[0][0] = 1
    for i in range(1, 1001):
        combination[i][0] = 1
        for j in range(1, i+1):
            combination[i][j] = (combination[i-1][j-1] + combination[i-1][j])%mod
calc()

for case in range(int(input())):
    N, M, T = map(int, input().split())
    wrong_prob = combination[N-M][T]
    correct_prob = combination[N][T]
    # fail_prob = wrong_prob/correct_prob
    # pass_prob = 1-fail_prob
    # print(pass_prob)
    numerator = correct_prob-wrong_prob
    denominator = correct_prob
    num_coprime = numerator//math.gcd(numerator, denominator)
    den_coprime = denominator//math.gcd(numerator, denominator)
    multiplicative_inverse = pow(den_coprime, (10**9+7)-2, (10**9+7))
    ans = (num_coprime*multiplicative_inverse)%(10**9+7)
    print(ans)
