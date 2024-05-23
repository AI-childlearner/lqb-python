n = int(input())
lis = list(map(int, input().split()))
res = [0]*n
tree = [0]*(4*n+1)
def point_alter(inx, va, node, l, r):      #单点修改
  if inx==l==r:
    tree[node] += va
    return tree[node]
  elif l>inx or r<inx:
    return tree[node]
  mid = (l+r)//2
  tree[node] = point_alter(inx, va, node*2, l, mid)+point_alter(inx, va, node*2+1, mid+1, r)
  return tree[node]

def inquire(node, l, r, a, b):         #区间查询
  if a<=l and r<=b:
    return tree[node]
  elif r<a or l>b or a>b:
    return 0
  mid = (l+r)//2
  return inquire(node*2, l, mid, a, b)+inquire(node*2+1, mid+1, r, a, b)

dic = {}
for i in range(n):
  if lis[i] not in dic:
    dic[lis[i]] = i
    res[i] = str(-lis[i])
    point_alter(i, 1, 1, 0, n-1)
  else:
    res[i] = str(inquire(1, 0, n-1, dic[lis[i]]+1, i-1))
    point_alter(i, 1, 1, 0, n-1)
    point_alter(dic[lis[i]], -1, 1, 0, n-1)
    dic[lis[i]] = i
print(' '.join(res))
