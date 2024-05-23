import sys
def dfs(u, nodes, fa):  # 从s节点出发，找到这条路径的节点
    for v in paper[u]:
        if v == fa:  continue
        if v in nodes:  # 找到环路了
            print(*sorted(nodes))
            sys.exit(0)
        dfs(v, nodes + [v], u)
n = int(input())
paper = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    paper[a].append(b)
    paper[b].append(a)
for i in range(1, n+1):dfs(i, [], None)
