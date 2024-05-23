n = int(input())
a = [[0] * (n+1) for _ in range(n+1)]
f = [[[0] * (n+1) for _ in range(n+1)] for _ in range(2 * (n+1))]
while True:
    x, y, w = map(int, input().split())
    if x == y == w == 0:
        break
    a[x][y] += w
for k in range(2, 2 * n + 1):
    for i1 in range(1, n + 1):
        for i2 in range(1, n + 1):
            j1 = k - i1
            j2 = k - i2
            if j1 < 1 or j1 > n or j2 < 1 or j2 > n:
                continue
            w = a[i1][j1]
            if i1 != i2 or j1 != j2:
                w += a[i2][j2]
            f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2 - 1] + w)
            f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1 - 1][i2] + w)
            f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2 - 1] + w)
            f[k][i1][i2] = max(f[k][i1][i2], f[k - 1][i1][i2] + w)
print(f[2 * n][n][n])