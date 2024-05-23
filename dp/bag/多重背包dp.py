N = 6010
f = [0] * N

n, m = map(int, input().split())
for _ in range(n):
    w, v, s = map(int, input().split())
    for j in range(m, -1, -1):
        for k in range(1, s + 1):
            if k * w <= j:
                f[j] = max(f[j], f[j - k * w] + v * k)

print(f[m])
