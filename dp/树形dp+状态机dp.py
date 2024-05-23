from collections import deque
while True:
    try:
        n=int(input())
        dic={i:[] for i in range(n)}
        s={i for i in range(n)}
        q=deque()
        du=[0]*n
        for _ in range(n):
            arr=input().split()
            node=int(arr[0].split(":")[0])
            if len(arr)>1:
                for k in arr[1:]:
                    k=int(k)
                    dic[k].append(node)
                    s-={k}
                    du[node]+=1
            else:
                q.append(node)
        root=s.pop()
        dp=[[0,1] for _ in range(n)]
        while q:
            cur=q.popleft()
            if cur in dic:
                for father in dic[cur]:
                    dp[father][0]+=dp[cur][1]
                    dp[father][1]+=min(dp[cur])
                    du[father]-=1
                    if du[father]==0:
                        q.append(father)
        print(min(dp[root]))
    except:
        break

