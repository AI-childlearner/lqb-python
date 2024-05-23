dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def dfs(x, y):
    if x == ex and y == ey:
        return True
    st[x][y] = True
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if a < 1 or a > n or b < 1 or b > n:
            continue
        if g[a][b] == 1 or st[a][b]:
            continue
        if dfs(a, b):
            return True
    return False

T = int(input())
for _ in range(T):
    n = int(input())
    g = [[0] * (n + 1) for _ in range(n + 1)]
    st = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        line = input()
        for j in range(1, n + 1):
            if line[j - 1] == '#':
                g[i][j] = 1
    sx, sy, ex, ey = map(int, input().split())
    sx += 1
    sy += 1
    ex += 1
    ey += 1
    if g[sx][sy] or g[ex][ey]:
        print("NO")
        continue
    if dfs(sx, sy):
        print("YES")
    else:
        print("NO")
from collections import deque

N = 110
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def main():
    K = int(input())
    for _ in range(K):
        n = int(input())
        g = [[0] * N for _ in range(N)]
        for i in range(1, n + 1):
            row = input()
            for j, ch in enumerate(row):
                if ch == '#':
                    g[i][j + 1] = 1

        sx, sy, ex, ey = map(int, input().split())
        sx, sy, ex, ey = sx + 1, sy + 1, ex + 1, ey + 1

        if g[sx][sy] or g[ex][ey]:
            print("NO")
            continue

        q = deque([(sx, sy)])
        vis = [[False] * N for _ in range(N)]
        ans = False

        while q:
            t = q.popleft()
            if t[0] == ex and t[1] == ey:
                ans = True
                break
            for i in range(4):
                a, b = t[0] + dx[i], t[1] + dy[i]
                if a < 1 or a > n or b < 1 or b > n or g[a][b] or vis[a][b]:
                    continue
                vis[a][b] = True
                q.append((a, b))

        if ans:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
