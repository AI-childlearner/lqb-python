class SegmentTreeNode:
    def __init__(self):
        self.lc = 0
        self.rc = 0
        self.sum = 0

class PersistentSegmentTree:
    def __init__(self, n):
        self.n = n
        self.idx = 0
        self.root = [0] * (n + 1)
        self.tr = [SegmentTreeNode() for _ in range(4 * n + n * 17)]
    
    def push_up(self, u):
        self.tr[u].sum = self.tr[self.tr[u].lc].sum + self.tr[self.tr[u].rc].sum
    
    def build(self, l, r):
        u = self.idx + 1
        self.idx += 1
        if l == r:
            return u
        mid = (l + r) // 2
        self.tr[u].lc = self.build(l, mid)
        self.tr[u].rc = self.build(mid + 1, r)
        return u
    
    def insert(self, v, l, r, x):
        u = self.idx + 1
        self.idx += 1
        self.tr[u] = SegmentTreeNode()
        self.tr[u].lc = self.tr[v].lc
        self.tr[u].rc = self.tr[v].rc
        self.tr[u].sum = self.tr[v].sum
        if l == r:
            self.tr[u].sum += 1
            return u
        mid = (l + r) // 2
        if x <= mid:
            self.tr[u].lc = self.insert(self.tr[u].lc, l, mid, x)
        else:
            self.tr[u].rc = self.insert(self.tr[u].rc, mid + 1, r, x)
        self.push_up(u)
        return u
    
    def query(self, u, v, l, r, k):
        if l == r:
            return l
        x = self.tr[self.tr[u].lc].sum - self.tr[self.tr[v].lc].sum
        mid = (l + r) // 2
        if k <= x:
            return self.query(self.tr[u].lc, self.tr[v].lc, l, mid, k)
        else:
            return self.query(self.tr[u].rc, self.tr[v].rc, mid + 1, r, k - x)

def main():
    import sys
    n,t = map(int,input().split())
    a = [0] + list(map(int,input().split()))
    b = [0] * (n + 1)
    for i in range(1, n + 1):
        b[i] = a[i]    
    b = sorted(set(b[1:n+1]))
    m = len(b)
    b = [0] + b
    
    pst = PersistentSegmentTree(n)
    pst.root[0] = pst.build(1, m)
    
    for i in range(1, n + 1):
        a[i] = b.index(a[i])
        pst.root[i] = pst.insert(pst.root[i - 1], 1, m, a[i])
    
    results = []
    for _ in range(t):
        l,r,k=map(int,input().split())
        result = b[pst.query(pst.root[r], pst.root[l - 1], 1, m, k)]
        results.append(result)
    
    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
