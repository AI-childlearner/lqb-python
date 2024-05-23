class Seg:
    def __init__(self, x, l, r, k):
        self.x = x
        self.l = l
        self.r = r
        self.k = k

    def __lt__(self, other):
        if self.x != other.x:
            return self.x < other.x
        return self.k > other.k

class Node:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.len1 = 0
        self.len2 = 0
        self.cnt = 0

def get(x, v):
    return v.index(x)

def pushup(u, tr, v):
    if tr[u].cnt:
        if tr[u].cnt & 1:
            tr[u].len1 = tr[u << 1].len2 + tr[u << 1 | 1].len2
            tr[u].len2 = tr[u << 1].len1 + tr[u << 1 | 1].len1
            tr[u].len1 += v[tr[u].r + 1] - v[tr[u].l] - tr[u].len1 - tr[u].len2
        else:
            tr[u].len1 = tr[u << 1].len1 + tr[u << 1 | 1].len1
            tr[u].len2 = tr[u << 1].len2 + tr[u << 1 | 1].len2
            tr[u].len2 += v[tr[u].r + 1] - v[tr[u].l] - tr[u].len1 - tr[u].len2
    elif tr[u].l != tr[u].r:
        tr[u].len1 = tr[u << 1].len1 + tr[u << 1 | 1].len1
        tr[u].len2 = tr[u << 1].len2 + tr[u << 1 | 1].len2
    else:
        tr[u].len1 = tr[u].len2 = 0

def build(u, l, r, tr):
    if l == r:
        tr[u] = Node(l, r)
        return
    mid = (l + r) // 2
    tr[u] = Node(l, r)
    build(u << 1, l, mid, tr)
    build(u << 1 | 1, mid + 1, r, tr)

def mdf(u, l, r, k, tr):
    if tr[u].l >= l and tr[u].r <= r:
        tr[u].cnt += k
        pushup(u, tr, v)
        return
    mid = tr[u].l + tr[u].r >> 1
    if l <= mid:
        mdf(u << 1, l, r, k, tr)
    if r > mid:
        mdf(u << 1 | 1, l, r, k, tr)
    pushup(u, tr, v)

n = int(input())
v = []
seg = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    v.extend([b, d])
    seg.append(Seg(a, b, d, 1))
    seg.append(Seg(c, b, d, -1))

v = sorted(set(v))
tr = [None] * ((len(v) - 1) * 4 + 1)  # Adjusted the size of tr array
build(1, 0, len(v) - 2, tr)
seg.sort()
def mul(a, b, p):
    ans = 0
    while b:
        if b & 1:
            ans = (ans + a) % p
        a = (a << 1) % p
        b >>= 1
    return ans

if __name__ == "__main__":
    a, b, p = map(int, input().split())
    print(mul(a, b, p))

res1 = 0
res2 = 0
for i in range(len(seg)):
    if i:
        res1 += 1 * (seg[i].x - seg[i - 1].x) * tr[1].len1
        res2 += 1 * (seg[i].x - seg[i - 1].x) * tr[1].len2
    mdf(1, get(seg[i].l, v), get(seg[i].r, v) - 1, seg[i].k, tr)

print(res1)
print(res2)
