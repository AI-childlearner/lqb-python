from collections import deque

# 定义方向
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 定义队列元素
class PII:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# BFS函数
def bfs():
    q = deque()
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if g[i][j]:
                q.append(PII(i, j))
    while q:
        t = q.popleft()
        for i in range(4):
            a = t.x + dx[i]
            b = t.y + dy[i]
            if a < 1 or a > n or b < 1 or b > m or g[a][b] or dist[a][b]:
                continue
            dist[a][b] = dist[t.x][t.y] + 1
            q.append(PII(a, b))

# 主函数
if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[0] * (m + 1) for _ in range(n + 1)]
    dist = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        row = input()
        for j in range(1, m + 1):
            g[i][j] = int(row[j - 1])
    bfs()
    for i in range(1, n + 1):
        print(*(dist[i][1:]))
