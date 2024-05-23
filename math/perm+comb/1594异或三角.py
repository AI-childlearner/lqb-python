t = int(input())

for _ in range(t):
    num = int(input())
    beg = 30
    dp = [0] * 3
    p = [0] * 3

    while (num & (1 << beg)) == 0:
        beg -= 1

    for i in range(beg, -1, -1):
        dp[2] = dp[2] * 4 + dp[1]
        dp[1] = dp[1] * 3 + dp[0] * 2
        dp[0] = dp[0] * 2

        if num & (1 << i):
            dp[2] += p[1] + 2 * p[2]
            p[2] *= 2
            dp[0] += p[0]
            dp[1] += p[1]
            p[1] = p[1] * 2 + p[0] * 2
        else:
            p[2] = p[2] * 2 + p[1]

        if p[0] == 0:
            p[0] = 3
        else:
            dp[0] += 3

    print(dp[2] + p[2])
