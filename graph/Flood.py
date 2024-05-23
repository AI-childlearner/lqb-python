# 设置递归深度限制
import sys
sys.setrecursionlimit(2000)

# 定义网格的最大大小
N = 1010

# 定义移动方向的数组
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# 定义深度优先搜索函数
def dfs(x, y):
    g[x][y] = '.'
    for i in range(8):
        a, b = x + dx[i], y + dy[i]
        if a < 1 or a > n or b < 1 or b > m or g[a][b] == '.':
            continue
        g[a][b] = '.'
        dfs(a, b)

# 读取输入的网格大小
n, m = map(int, input().split())

# 初始化网格
g = [['.' for _ in range(m + 1)] for _ in range(n + 1)]

# 读取网格数据
for i in range(1, n + 1):
    row = input().strip()
    for j in range(1, m + 1):
        g[i][j] = row[j - 1]

# 初始化答案
ans = 0

# 遍历网格进行搜索
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if g[i][j] == 'W':
            ans += 1
            dfs(i, j)

# 输出答案
print(ans)
