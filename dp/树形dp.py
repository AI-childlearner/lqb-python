class TreeNode:
    def __init__(self):
        self.children = []
        self.weight = []


def add(u, v, c):
    tree[u].children.append(v)
    tree[u].weight.append(c)


def dfs(u, fa):
    for i in range(len(tree[u].children)):
        j = tree[u].children[i]
        if j == fa:
            continue
        dfs(j, u)
        if f[0][j] + tree[u].weight[i] > f[0][u]:
            f[1][u] = f[0][u]
            f[0][u] = f[0][j] + tree[u].weight[i]
        elif f[0][j] + tree[u].weight[i] > f[1][u]:
            f[1][u] = f[0][j] + tree[u].weight[i]
    global ans
    ans = max(ans, f[0][u] + f[1][u])


n = int(input())
N = 10010
tree = [TreeNode() for _ in range(N)]
f = [[0] * N for _ in range(2)]
idx = 0
ans = 0

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    add(a, b, c)
    add(b, a, c)

dfs(1, -1)
print(ans)
