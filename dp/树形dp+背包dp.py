# 这题特殊在价值在边上，不是在点上，选了儿子才形成一条边，才占1体积，不选儿子不占
# 枚举分给儿子的体积时，必须要考虑父子之间需要一条边
# 所以k最大只能到j-1
n,m = map(int,input().split())
from collections import defaultdict
g = defaultdict(list)
for _ in range(n - 1):
    a,b,c = map(int,input().split())
    g[a].append((b,c))
    g[b].append((a,c))

f = [[0]*(m + 1) for _ in range(n + 1)]

def dfs(u,fa):
    for v,w in g[u]:
        if v == fa:
            continue
        dfs(v,u)
        for j in range(m,0,-1):# 枚举到1即可，不选儿子不用算了，肯定是0
            for k in range(j): # 选v，则uv需要占用一条边，所以最大j - 1
                f[u][j] = max(f[u][j],f[u][j - k - 1] + f[v][k] + w)

dfs(1,-1)
print(f[1][-1])

