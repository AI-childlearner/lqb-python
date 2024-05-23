MOD = int(1E9 + 7)


def ans0(x, y):
    if x < 0 or y < 0:
        return 0
    if x <= y:
        return (x % MOD + 2) * (x % MOD + 1) // 2 % MOD
    x %= MOD
    y %= MOD
    return ((y + 2) * (y + 1) // 2 % MOD + (x - y) * (y + 1) % MOD) % MOD


def ans1(x, y):
    return min(x, y) + 1


def ans2(x, y):
    return max(x - y + 1, 0)


t, k = map(int, input().split())
for _ in range(t):
    n, m = map(int, input().split())
    if m > n:
        m = n
    ans = ans0(n, m)
    a = [0] * 70
    b = [0] * 70
    lena = 0
    lenb = 0
    while n:
        n, r = divmod(n, k)
        a[lena] = r
        lena += 1
    while m:
        m, r = divmod(m, k)
        b[lenb] = r
        lenb += 1
    n = lena
    dp = [[0] * 4 for _ in range(n + 1)]
    dp[n][3] = 1
    for i in range(n - 1, -1, -1):
        dp[i][0] = dp[i + 1][0] * ans0(k - 1, k - 1)
        dp[i][0] += dp[i + 1][1] * ans0(a[i] - 1, k - 1) + dp[i + 1][2] * ans0(k - 1, b[i] - 1)
        dp[i][0] += dp[i + 1][3] * ans0(a[i] - 1, b[i] - 1)

        dp[i][1] = dp[i + 1][1] * ans1(a[i], k - 1) + dp[i + 1][3] * ans1(a[i], b[i] - 1)

        dp[i][2] = dp[i + 1][2] * ans2(k - 1, b[i]) + dp[i + 1][3] * ans2(a[i] - 1, b[i])

        dp[i][3] = ((a[i] >= b[i]) and dp[i + 1][3])
        for j in range(4):
            dp[i][j] %= MOD
    ans -= dp[0][0] + dp[0][1] + dp[0][2] + dp[0][3]
    ans = (ans % MOD + MOD) % MOD
    print(ans)