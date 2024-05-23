N = 1010
f = [0] * N
n, m = map(int, input().split())

for _ in range(n):
    w, v, s = map(int, input().split())
    if not s:
        for j in range(w, m + 1)[::-1]:
            f[j] = max(f[j], f[j - w] + v)
    else:
        s = abs(s)
        k = 1
        while s > 0:
            for j in range(m, w * k - 1, -1):
                f[j] = max(f[j], f[j - w * k] + v * k)
            s -= k
            k *= 2
        if s:
            for j in range(m, w * s - 1, -1):
                f[j] = max(f[j], f[j - w * s] + v * s)

print(f[m])
