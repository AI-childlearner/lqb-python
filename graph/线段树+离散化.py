import sys

LAST = False
N=100010
def read_input():
    global LAST
    if LAST:
        return ""
    s = sys.stdin.readline().strip()
    while not s and not LAST:
        s = sys.stdin.readline().strip()
    if not s:
        LAST = True
    return s

class SegmentTreeNode:
    def __init__(self, l, r, cnt, length):
        self.l = l
        self.r = r
        self.cnt = cnt
        self.length = length

def push_up(tree, u):
    if tree[u].cnt:
        tree[u].length = all_values[tree[u].r + 1] - all_values[tree[u].l]
    else:
        tree[u].length = tree[u << 1].length + tree[(u << 1) | 1].length

def build(tree, u, l, r):
    tree[u] = SegmentTreeNode(l, r, 0, 0)
    if l == r:
        return
    mid = (l + r) // 2
    build(tree, u << 1, l, mid)
    build(tree, (u << 1) | 1, mid + 1, r)

def modify(tree, u, l, r, c):
    if all_values[tree[u].r + 1] <= l or r <= all_values[tree[u].l]:
        return
    if l <= all_values[tree[u].l] and all_values[tree[u].r + 1] <= r:
        tree[u].cnt += c
        push_up(tree, u)
        return
    mid = tree[u].l + tree[u].r >> 1
    modify(tree, u << 1, l, r, c)
    modify(tree, (u << 1) | 1, l, r, c)
    push_up(tree, u)

T = 1
while True:
    n = int(read_input())
    if n == 0:
        break
    lines = []
    all_values = []
    for i in range(n):
        x1, y1, x2, y2 = map(float, read_input().split())
        lines.append((x1, x2, y1, 1))
        lines.append((x1, x2, y2, -1))
        all_values.extend([x1, x2])
    n <<= 1
    all_values.sort()
    lines.sort(key=lambda x: x[2])
    all_values = sorted(list(set(all_values)))
    m = len(all_values) - 1
    tree = [None] * (16 * N)
    build(tree, 1, 1, m - 1)
    ans = 0
    for i in range(n - 1):
        modify(tree, 1, lines[i][0], lines[i][1], lines[i][3])
        ans += tree[1].length * (lines[i + 1][2] - lines[i][2])
    print(f"Test case #{T}")
    print(f"Total explored area: {ans:.2f}")
    print()
    T += 1
