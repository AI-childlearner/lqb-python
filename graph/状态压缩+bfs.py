from collections import deque

N = 11
M = 360
P = 1 << 10
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
h = [0] * (N * N)
e = [-1] * M
ne = [-1] * M
w = [-1] * M
idx = 0
g = [[0] * N for _ in range(N)]
key = [0] * (N * N)
dist = [[float('inf')] * P for _ in range(N * N)]
st = [[False] * P for _ in range(N * N)]
edges = set()

def add(a, b, c):
    global idx
    e[idx] = b
    w[idx] = c
    ne[idx] = h[a]
    h[a] = idx
    idx += 1

def bfs():
    dist[1][0] = 0
    q = deque([(1, 0)])
    while q:
        t, state = q.popleft()
        if st[t][state]:
            continue
        st[t][state] = True
        if t == n * m:
            return dist[t][state]
        if key[t]:
            nstate = state | key[t]
            if dist[t][nstate] > dist[t][state]:
                dist[t][nstate] = dist[t][state]
                q.appendleft((t, nstate))
        i = h[t]
        while i != -1:
            j = e[i]
            if w[i] != -1 and not (state >> w[i] - 1 & 1):
                continue
            if dist[j][state] > dist[t][state] + 1:
                dist[j][state] = dist[t][state] + 1
                q.append((j, state))
            i = ne[i]
    return -1

n, m, p = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        g[i][j] = cnt = cnt + 1

t = int(input())
while t > 0:
    t -= 1
    x1, y1, x2, y2, c = map(int, input().split())
    a, b = g[x1][y1], g[x2][y2]
    edges.add((a, b))
    edges.add((b, a))
    if c:
        add(a, b, c)
        add(b, a, c)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        for u in range(4):
            x, y = i + dx[u], j + dy[u]
            if x < 1 or x > n or y < 1 or y > m:
                continue
            a, b = g[i][j], g[x][y]
            if (a, b) not in edges:
                add(a, b, 0)

t = int(input())
while t > 0:
    t -= 1
    x, y, c = map(int, input().split())
    key[g[x][y]] |= 1 << c - 1

print(bfs())
