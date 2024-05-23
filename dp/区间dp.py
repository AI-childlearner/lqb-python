n = int(input())
N = 410
a = list(map(int, input().split()))
a=a+a
a=[0]+a

s = [0] * (N) 
f = [[0] * (N) for _ in range(N)]
g = [[1e10] * (N) for _ in range(N)]

for i in range(1, 2 * n + 1):
    s[i] = s[i - 1] + a[i]
    f[i][i] = g[i][i] = 0

for length in range(2, n + 1):  # Enumerating up to n is enough
    for i in range(1, 2 * n - length + 2):
        j = i + length - 1
        for k in range(i, j):
            f[i][j] = max(f[i][j], f[i][k] + f[k + 1][j] + s[j] - s[i - 1])
            g[i][j] = min(g[i][j], g[i][k] + g[k + 1][j] + s[j] - s[i - 1])

ans1 = 0
ans2 = 2e9

for i in range(1, n + 2):
    ans1 = max(ans1, f[i][i + n - 1])
    ans2 = min(ans2, g[i][i + n - 1])

print(ans2)
print(ans1)
