# Python equivalent of the provided C++ code

N = 3010
n = int(input())
a = [0] * (N + 1)
b = [0] * (N + 1)
f = [[0] * (N + 1) for _ in range(N + 1)]

# Reading input
a[1:n + 1] = map(int, input().split())
b[1:n + 1] = map(int, input().split())

for i in range(1, n + 1):
    maxv = 1
    for j in range(1, n + 1):
        f[i][j] = max(f[i][j], f[i - 1][j])
        if a[i] == b[j]:
            f[i][j] = max(f[i][j], maxv)
        if b[j] < a[i]:
            maxv = max(maxv, f[i - 1][j] + 1)

ans = 0
for i in range(1, n + 1):
    ans = max(ans, f[n][i])

print(ans)

