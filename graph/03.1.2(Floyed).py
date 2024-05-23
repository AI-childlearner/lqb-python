import sys

N = 110
INF = float('inf')

n = m = ans = 0
g = [[INF] * N for _ in range(N)]

def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

def main():
    global n, m, ans
    n, m = map(int, input().split())
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                g[i][j] = 0
            else:
                g[i][j] = INF
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        g[a][b] = g[b][a] = min(g[a][b], c)
    
    floyd()
    
    for i in range(1, n + 1):
        if g[1][i] == INF:
            ans = -1
            break
        ans = max(ans, g[1][i])
    
    print(ans)

if __name__ == "__main__":
    main()
