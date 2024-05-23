m = 1010
n, m = map(int, input().split())
f = [0] * (m + 1)

for i in range(n):
    w, v = map(int, input().split())
    for j in range(m, w - 1, -1):
        f[j] = max(f[j], f[j - w] + v)

print(f[m])
