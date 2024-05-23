from collections import deque

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = s[i - 1] + a[i - 1]

ans = float("-inf")
q = deque([0])

for i in range(1, n + 1):
    while q and i - q[0] > m:
        q.popleft()
    ans = max(ans, s[i] - s[q[0]])
    while q and s[q[-1]] >= s[i]:
        q.pop()
    q.append(i)

print(ans)
