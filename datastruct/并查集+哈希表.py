from collections import defaultdict

neq = []  # 不等式表
ori = defaultdict(int)  # 并查集用源节点表
idx = {}  # 用于映射索引的字典
tot = 1  # tot每次给新出现的变量赋索引之后都会自增（不用这个也许可以）

def get_index(x):
    global tot
    # 未曾出现过的需要赋予新索引
    if x not in idx:
        idx[x] = tot
        tot += 1
    return idx[x]

def find(x):
    # 针对索引值查找
    if x != ori[x]:
        ori[x] = find(ori[x])
    return ori[x]

def is_equal(x, y):
    # 判断变量是否相等
    return find(get_index(x)) == find(get_index(y))

def equalize(x, y):
    # 使两个变量相等
    pr = find(get_index(x))
    nx = find(get_index(y))
    if pr != nx:
        ori[pr] = nx

t = int(input())
for _ in range(t):
    # 每组测试用例分别独立，需要清空 idx 和 neq
    idx.clear()
    neq.clear()
    tot = 1
    n = int(input())
    ori = defaultdict(int)
    for _ in range(n):
        i, j, e = map(int, input().split())
        if e == 1:
            equalize(i, j)  # 等式，直接让他俩相等
        else:
            neq.append((i, j))  # 不等式，脱机处理
    res = "YES"
    # 遍历不等式
    for i, j in neq:
        # 本应不等却相等，无法成立
        if is_equal(i, j):
            res = "NO"
            break
    print(res)
