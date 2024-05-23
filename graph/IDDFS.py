N = 10010
path = [0] * N

def dfs(u, depth):
    if u > depth:
        return False
    if path[u - 1] == n:
        return True
    if path[u - 1] * (1 << (depth - u + 1)) < n:
        return False
    st = [False] * N
    for i in range(u):
        for j in range(i + 1):
            total = path[i] + path[j]
            if total > n or total <= path[u - 1] or st[total]:
                continue
            st[total] = True
            path[u] = total
            if dfs(u + 1, depth):
                return True
    return False

while True:
    n = int(input())
    if n == 0:
        break
    path[0] = 1
    depth = 1
    while not dfs(1, depth):
        depth += 1
    print(*path[:depth])
