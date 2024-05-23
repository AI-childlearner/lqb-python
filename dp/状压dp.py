N = 12
M = 1 << N
state = []
h = [[] for _ in range(M)]
cnt = [0] * M
f = [[[0] * M for _ in range(N * N)] for _ in range(N)]

def check(x):
    for i in range(n - 1):
        if (x >> i & 1) and (x >> (i + 1) & 1):
            return False
    return True

def count(x):
    return bin(x).count('1')

n, m = map(int, input().split())
for i in range(1 << n):
    if check(i):
        state.append(i)
        cnt[i] = count(i)

for i in range(len(state)):
    for j in range(len(state)):
        a, b = state[i], state[j]
        if (a & b) == 0 and check(a | b):
            h[i].append(j)

f[0][0][0] = 1
for i in range(1, n + 2):
    for j in range(m + 1):
        for a in range(len(state)):
            for b in h[a]:
                c = cnt[state[a]]
                if j >= c:
                    f[i][j][a] += f[i - 1][j - c][b]

print(f[n + 1][m][0])
