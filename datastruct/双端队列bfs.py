from collections import deque

dx = [-1, -1, 1, 1]
dy = [-1, 1, 1, -1]
ix = [-1, -1, 0, 0]
iy = [-1, 0, 0, -1]
dirs = ['\\', '/', '\\', '/']

def bfs():
    q = deque([(0, 0)])
    dist = [[float('inf')] * (m + 1) for _ in range(n + 1)]
    vis = [[False] * (m + 1) for _ in range(n + 1)]
    dist[0][0] = 0

    while q:
        t = q.popleft()
        if t == (n, m):
            return dist[t[0]][t[1]]
        if vis[t[0]][t[1]]:
            continue
        vis[t[0]][t[1]] = True
        for i in range(4):
            a, b = t[0] + dx[i], t[1] + dy[i]
            if 0 <= a <= n and 0 <= b <= m:
                ga, gb = t[0] + ix[i], t[1] + iy[i]
                w = 0 if g[ga][gb] == dirs[i] else 1
                d = dist[t[0]][t[1]] + w
                if d <= dist[a][b]:
                    dist[a][b] = d
                    if not w:
                        q.appendleft((a, b))
                    else:
                        q.append((a, b))
    return -1

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    g = [input() for _ in range(n)]
    if (n + m) % 2 == 1:
        print("NO SOLUTION")
    else:
        print(bfs())
