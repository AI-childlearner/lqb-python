import heapq

N = 1010
M = 200010

h = [[] for _ in range(N)]
rh = [[] for _ in range(N)]
dist = [float('inf')] * N
cnt = [0] * N
st = [False] * N

def add(h, a, b, c):
    h[a].append((b, c))

def dijkstra():
    global dist
    heap = [(0, T)]
    dist[T] = 0
    while heap:
        d, ver = heapq.heappop(heap)
        if st[ver]:
            continue
        st[ver] = True
        for j, w in rh[ver]:
            if dist[j] > dist[ver] + w:
                dist[j] = dist[ver] + w
                heapq.heappush(heap, (dist[j], j))

def Astar():
    heap = [(dist[S], 0, S)]
    while heap:
        distance, cnt_ver, ver = heapq.heappop(heap)
        cnt[ver] += 1
        if cnt[T] == K:
            return distance
        for j, w in h[ver]:
            if cnt[j] < K:
                heapq.heappush(heap, (distance + w + dist[j], 0, j))
    return -1

if __name__ == "__main__":
    n, m = map(int, input().split())
    for _ in range(m):
        a, b, c = map(int, input().split())
        add(h, a, b, c)
        add(rh, b, a, c)
    S, T, K = map(int, input().split())
    if S == T:
        K += 1
    dijkstra()
    print(Astar())
