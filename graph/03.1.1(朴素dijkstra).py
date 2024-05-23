import sys

N = 2510

def dijkstra(n, m, st, ed, g):
    dist = [float('inf')] * (n + 1)
    dist[st] = 0
    vis = [False] * (n + 1)
    
    for _ in range(1, n + 1):
        t = -1
        for j in range(1, n + 1):
            if not vis[j] and (t == -1 or dist[t] > dist[j]):
                t = j
        vis[t] = True
        for j in range(1, n + 1):
            dist[j] = min(dist[j], dist[t] + g[t][j])
    
    return dist[ed]

def main():
    n, m, st, ed = map(int, input().split())
    g = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a][b] = g[b][a] = min(g[a][b], c)
    
    ans = dijkstra(n, m, st, ed, g)
    print(ans)

if __name__ == "__main__":
    main()
