import heapq

start = input().replace(' ', '')
seq = start.replace('x', '')

def f(state):
    res = 0
    # for i in range(len(state)):
    #     if state[i] != 'x':
    #         t = ord(state[i])
    #         res += abs(i // 3 - t // 3) + abs(i % 3 - t % 3);
    return res

def bfs(start):
    end, op = "12345678x", "urdl"
    dist, prev = {}, {}
    heap = []
    dist[start] = 0
    heapq.heappush(heap, (f(start), start))
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    while heap:
        t, state = heapq.heappop(heap)
        if start == end: break
        x, y = 0, 0
        for i in range(9):
            if state[i] == 'x':
                x, y = i // 3, i % 3
                break
        source = state
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if a < 0 or a >= 3 or b < 0 or b >= 3: continue
            ss = source
            z, p = ss[x * 3 + y], ss[a * 3 + b]
            ss = ss.replace(z, 'q')
            ss = ss.replace(p, z)
            ss = ss.replace('q', p)
            if (ss not in dist or dist[ss] > dist[source] + 1):
                dist[ss] = dist[source] + 1
                prev[ss] = (op[i], source)
                heapq.heappush(heap, (dist[ss] + f(ss), ss))
    res = ""
    while end != start:
        xx, yy = prev[end]
        res += xx
        end = yy
    return res[::-1]        
cnt = 0
for i in range(8):
    for j in range(i, 8):
        if seq[i] > seq[j]:
            cnt += 1
if cnt & 1: print("unsolvable")
else: print(bfs(start))
