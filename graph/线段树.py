class SegmentTreeNode:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.v = 0

def pushup(tree, u):
    tree[u].v = max(tree[u * 2].v, tree[u * 2 + 1].v)

def build(tree, u, l, r):
    tree[u] = SegmentTreeNode(l, r)
    if l == r:
        return
    mid = (l + r) // 2
    build(tree, u * 2, l, mid)
    build(tree, u * 2 + 1, mid + 1, r)

def fix(tree, u, x, v):
    if tree[u].l == x and tree[u].r == x:
        tree[u].v = v
    else:
        mid = (tree[u].l + tree[u].r) // 2
        if x <= mid:
            fix(tree, u * 2, x, v)
        else:
            fix(tree, u * 2 + 1, x, v)
        pushup(tree, u)

def query(tree, u, l, r):
    if tree[u].l >= l and tree[u].r <= r:
        return tree[u].v
    mid = (tree[u].l + tree[u].r) // 2
    ans = 0
    if l <= mid:
        ans = max(ans, query(tree, u * 2, l, r))
    if r > mid:
        ans = max(ans, query(tree, u * 2 + 1, l, r))
    return ans

n = 0
m, p = map(int, input().split())
tree = [None] * (4 * m)
build(tree, 1, 1, m)
last = 0
for _ in range(m):
    ch, x = input().split()
    x = int(x)
    if ch == 'A':
        n += 1
        fix(tree, 1, n, (last + x) % p)
    else:
        last = query(tree, 1, n - x + 1, n)
        print(last)
