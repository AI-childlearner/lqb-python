def dfs(x, y, t, n, m, vis):
    if t == n * m:
        return 1
    ans = 0
    dx = [1, -1, 2, -2, 1, -1, 2, -2]
    dy = [2, 2, 1, 1, -2, -2, -1, -1]
    for i in range(8):
        a = x + dx[i]
        b = y + dy[i]
        if 1 <= a <= n and 1 <= b <= m and not vis[a][b]:
            vis[a][b] = True
            ans += dfs(a, b, t + 1, n, m, vis)
            vis[a][b] = False
    return ans

def main():
    t = int(input())
    for _ in range(t):
        n, m, sx, sy = map(int, input().split())
        sx += 1
        sy += 1
        vis = [[False] * (m + 1) for _ in range(n + 1)]
        vis[sx][sy] = True
        ans = dfs(sx, sy, 1, n, m, vis)
        print(ans)

if __name__ == "__main__":
    main()
