class Edge:
    def __init__(self, a, b, w):
        self.a = a
        self.b = b
        self.w = w

n = int(input())
N = 110
M = 10010
edges = []
p = [i for i in range(N)]

def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]

def kruskal():
    edges.sort(key=lambda edge: edge.w)
    ans = 0
    for edge in edges:
        a, b, w = edge.a, edge.b, edge.w
        a = find(a)
        b = find(b)
        if a != b:
            p[a] = b
            ans += w
    return ans

for i in range(1, n + 1):
    weights = list(map(int, input().split()))
    for j in range(1, n + 1):
        x = weights[j - 1]
        edges.append(Edge(i, j, x))

print(kruskal())
