from collections import deque

# 染色法判断二分图，交替的为相邻节点染色
# 如果遇到了相邻同色的情况，就说明这个图不是二分图
def check(limit):
    colors = [0] * (n + 1)
    for i in range(1, n + 1):
        if colors[i] == 0:
            q = deque()
            q.append(i)
            colors[i] = 1
            while q:
                cur = q.popleft()
                for nx, val in adjList[cur]:
                    if val > limit:
                        if colors[nx] == 0:
                            colors[nx] = -colors[cur]
                            q.append(nx)
                        if colors[nx] == colors[cur]:
                            return False
    return True

n, m = map(int, input().split())
adjList = [[] for _ in range(n + 1)]
mv = 0

for _ in range(m):
    s, e, v = map(int, input().split())
    adjList[s].append((e, v))
    adjList[e].append((s, v))
    mv = max(v, mv)

low, high = 0, mv

while low < high:
    mid = (low + high) // 2
    if check(mid):
        high = mid
    else:
        low = mid + 1

print(low)
