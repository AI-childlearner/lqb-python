from collections import deque

N = 110
M = 10010
INF = float('inf')

h = [-1] * N
e = [0] * M
w = [0] * M
ne = [0] * M
idx = 0

L = [0] * N
dist = [INF] * N
st = [False] * N

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def spfa(l, r):
    global idx
    global dist
    global st
    dist = [INF] * N
    st = [False] * N
    dist[0] = 0
    q = deque()
    q.append(0)
    while q:
        t = q.popleft()
        st[t] = False
        i = h[t]
        while i != -1:
            j = e[i]
            if l <= L[j] <= r and dist[j] > dist[t] + w[i]:
                dist[j] = dist[t] + w[i]
                if not st[j]:
                    q.append(j)
                    st[j] = True
            i = ne[i]
    return dist[1]

h = [-1] * N
m, n = map(int, input().split())
for i in range(1, n + 1):
    x, L[i], k = map(int, input().split())
    add(0, i, x)
    for _ in range(k):
        x, w = map(int, input().split())
        add(x, i, w)

ans = INF
for i in range(L[1] - m, L[1] + 1):
    ans = min(ans, spfa(i, i + m))

print(ans)
