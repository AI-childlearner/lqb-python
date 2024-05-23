 
# 读入点权和边权
L,P = map(int,input().split())
lst = [0]
for i in range(L) : lst.append(int(input()))
Map = [[0 for i in range(L+1)]for j in range(L+1)]
for i in range(P) : 
    a,b,c = map(int,input().split())
    Map[a][b] = c
    
def check(mid) : # spfa
    flag = [1 for i in range(L+1)] # 队列里是否有这个元素
    cnt = [0 for i in range(L+1)] # 计数
    queue = [i for i in range(1,L+1)]
    dis = [0 for i in range(L+1)]
    while queue :
        node = queue.pop(0)
        flag[node] = 0
        for i in range(1,L+1) :
            if Map[node][i] :
                new_dis = dis[node] + lst[node] - Map[node][i]*mid
                if dis[i] < new_dis : # 注意这里是求最长路，因为是要判断是否存在正环
                    dis[i] = new_dis
                    cnt[i] = cnt[node] + 1
                    if cnt[i] >= L : return True # 存在正环
                    if not flag[i] : queue.append(i);  flag[i] = 1 # 如果这个点不在队列里，加入队列
    return False
    
left,right,eps = 0,1010,10**(-4) # 二分答案
while right - left > eps :
    mid = (left+right)/2
    if check(mid) : left = mid
    else : right = mid
print('%.2f'%right)
