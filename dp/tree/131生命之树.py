import sys
sys.setrecursionlimit(100000)
n=int(input())
aList=[0] + [int(i) for i in input().split()]
tree=[[]for i in range(n+1)]
root_max=[0 for i in range(n+1)]
for i in range(n-1):
    m,n=map(int,input().split())
    tree[m].append(n)
    tree[n].append(m)
def dfs(dad,son):
    root_max[son]=aList[son]
    for i  in tree[son]:
        if i !=dad:
            root_max[i]=dfs(son,i)
            if root_max[i]>0:
                root_max[son]+=root_max[i]
    return root_max[son]
dfs(0,1)
print(max(root_max))