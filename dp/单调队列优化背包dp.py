n, m = map(int, input().split())
N = 20010
f = [[0] * N for _ in range(2)]
q = [0] * N
hh = 0
tt = -1

for i in range(1,n+1):
    w, v, s = map(int, input().split())
    for r in range(w):
        hh = 0
        tt = -1
        for j in range(r, m + 1, w):
            while hh <= tt and q[hh] < j - w * s:
                hh += 1
            while hh <= tt and f[(i - 1) % 2][q[tt]] + (j - q[tt]) // w * v <= f[(i - 1) % 2][j]:
                tt -= 1
            tt += 1
            q[tt] = j
            f[i % 2][j] = f[(i - 1) % 2][q[hh]] + (j - q[hh]) // w * v

print(f[n % 2][m])
