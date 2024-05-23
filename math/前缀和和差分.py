N = 5010
n = 5005
m, r = map(int, input().split())
sum = [[0] * N for _ in range(N)]

def get(x1, y1, x2, y2):
    return sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1]

maxx = 0
maxy = 0
for _ in range(m):
    x, y, w = map(int, input().split())
    x += 1
    y += 1
    maxx = max(maxx, x)
    maxy = max(maxy, y)
    sum[x][y] += w

for i in range(1, n + 1):
    for j in range(1, n + 1):
        sum[i][j] += sum[i][j - 1] + sum[i - 1][j] - sum[i - 1][j - 1]

if r >= maxx and r >= maxy:
    print(sum[n][n])
    exit()

ans = 0
for i in range(1, n - r + 2):
    for j in range(1, n - r + 2):
        ans = max(ans, get(i, j, i + r - 1, j + r - 1))

print(ans)
