from collections import deque

N = 405

# path用来求传递闭包，其余用来求最大匹配值
val = [[0] * N for _ in range(N)]
path = [[0] * (N // 2) for _ in range(N // 2)]
pre = [-1] * N
vis = [0] * N

n, m = map(int, input().split())
for _ in range(m):
    s, e = map(int, input().split())
    path[s][e] = 1
    val[s][200 + e] = 1

# 求传递闭包之后会产生新边
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if path[i][k] == 1 and path[k][j] == 1:
                path[i][j] = 1
                val[i][200 + j] = 1

# 加上公共始端和公共终端
source = 0
terminal = N - 1
for i in range(1, n + 1):
    val[source][i] = val[200 + i][terminal] = 1

# 求最大匹配（其实就是求从始端S到终端T的网络最大流）
def findPath(source, terminal):
    global vis, pre
    vis = [0] * N
    pre = [-1] * N
    q = deque()
    q.append(source)
    vis[source] = 1
    while q:
        cur = q.popleft()
        for i in range(N):
            if vis[i] == 0 and val[cur][i] > 0:
                vis[i] = 1
                pre[i] = cur
                if i == terminal:
                    return True
                q.append(i)
    return False

def maxFlow(source, terminal):
    sum_flow = 0
    while findPath(source, terminal):
        last = -1
        now = terminal
        sum_flow += 1
        while now != source:
            last = pre[now]
            val[last][now] -= 1
            val[now][last] += 1
            now = last
    return sum_flow

# 结果为节点总数减去最大匹配数（最大流量）
print(n - maxFlow(source, terminal))
