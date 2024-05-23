import sys

N = 110
INF = float('inf')

def prim(n, g):
    dist = [INF] * (n + 1)
    ans = 0
    st = [False] * (n + 1)
    
    for i in range(n):
        t = -1
        for j in range(1, n + 1):
            if not st[j] and (t == -1 or dist[t] > dist[j]):
                t = j
        if i > 0 and dist[t] == INF:
            return INF
        if i > 0:
            ans += dist[t]
        st[t] = True
        for j in range(1, n + 1):
            dist[j] = min(dist[j], g[t][j])
    
    return ans

def main():
    n = int(input())
    g = [[0] * (N + 1) for _ in range(N + 1)]
    
    for i in range(1, n + 1):
        row = list(map(int, input().split()))
        for j in range(1, n + 1):
            g[i][j] = row[j - 1]
    
    print(prim(n, g))

if __name__ == "__main__":
    main()
