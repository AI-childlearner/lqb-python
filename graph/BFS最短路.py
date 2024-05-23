from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(n, g):
    queue = deque([(n, n)])
    pre = [[-1] * (n + 1) for _ in range(n + 1)]
    pre[n][n] = (1, 1)

    while queue:
        t = queue.popleft()
        for i in range(4):
            a, b = t[0] + dx[i], t[1] + dy[i]
            if 1 <= a <= n and 1 <= b <= n and not g[a][b] and pre[a][b] == -1:
                queue.append((a, b))
                pre[a][b] = t

    return pre

def main():
    n = int(input())
    g = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        g[i][1:n + 1] = map(int, input().split())

    pre = bfs(n, g)
    end = (1, 1)

    while True:
        print(end[0] - 1, end[1] - 1)
        if end == (n, n):
            break
        end = pre[end[0]][end[1]]

if __name__ == "__main__":
    main()
