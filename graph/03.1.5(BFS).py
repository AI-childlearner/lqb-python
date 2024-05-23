from collections import deque

N = 510
INF = float('inf')

def bfs():
    q = deque([1])
    dist = [INF] * (n + 1)
    dist[1] = 0
    while q:
        t = q.popleft()
        for i in range(1, n + 1):
            if g[t][i] and dist[i] > dist[t] + 1:
                dist[i] = dist[t] + 1
                q.append(i)
    return dist[n]

m, n = map(int, input().split())
g = [[False] * (N + 1) for _ in range(N + 1)]
for _ in range(m):
    stops = list(map(int, input().split()))
    for i in range(len(stops)):
        for j in range(i + 1, len(stops)):
            g[stops[i]][stops[j]] = True

ans = bfs()
if ans == INF:
    print("NO")
else:
    print(max(ans - 1, 0))
