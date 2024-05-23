import heapq
n,m = map(int,input().split())
g = [[] for _ in range(n+1)]
d = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split())
    g[a].append((b,c)); d[b].append((a,c))

s,t,k = map(int,input().split())
if s == t: k += 1

# 反着做dij
dist = [float('inf')]*(n+1)
def dij():
    q = [(t,0)]
    dist[t] = 0
    while q:
        cur,costs = heapq.heappop(q)
        if dist[cur] < costs: continue
        for pre,w in d[cur]:
            if dist[pre] > dist[cur] + w:
                dist[pre] = dist[cur] + w
                heapq.heappush(q,(pre,dist[pre]))
def astar():
    q = [(dist[s],(0,s))]
    count = 0
    if dist[s] == float('inf'): return -1
    while q:
        dt,cur = heapq.heappop(q)[1]
        if cur == t:count +=1
        if count == k: return dt
        for next,w in g[cur]:
            heapq.heappush(q,(dt+w+dist[next],(dt+w,next)))
    return -1
dij()
print(astar())
