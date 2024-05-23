MOD = 200907

def power(a, b, p):
    ans = 1
    while b:
        if b & 1:
            ans = ans * a % p
        a = a * a % p
        b >>= 1
    return ans

T = int(input())
for _ in range(T):
    a, b, c, n = map(int, input().split())
    if b - a == c - b:
        print((a + (b - a) * (n - 1)) % MOD)
    else:
        print(a * power(b // a, n - 1, MOD) % MOD)
