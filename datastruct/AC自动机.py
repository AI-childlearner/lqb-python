from collections import deque

N = 10010
S = 55
M = 1000010

tr = [[0] * 26 for _ in range(N * S)]
cnt = [0] * (N * S)
fail = [0] * (N * S)
idx = 0

def insert(s):
    global idx
    p = 0
    for char in s:
        x = ord(char) - ord('a')
        if not tr[p][x]:
            idx += 1
            tr[p][x] = idx
        p = tr[p][x]
    cnt[p] += 1

def get_fail():
    global idx
    q = deque()
    for i in range(26):
        if tr[0][i]:
            q.append(tr[0][i])
    while q:
        t = q.popleft()
        for i in range(26):
            p = tr[t][i]
            if not p:
                tr[t][i] = tr[fail[t]][i]
            else:
                fail[p] = tr[fail[t]][i]
                q.append(p)

def main():
    T = int(input())
    for _ in range(T):
        global idx
        idx = 0
        tr.clear()
        cnt.clear()
        fail.clear()
        tr = [[0] * 26 for _ in range(N * S)]
        cnt = [0] * (N * S)
        fail = [0] * (N * S)

        n = int(input())
        for _ in range(n):
            x = input()
            insert(x)
        get_fail()
        str = input()
        ans = 0
        j = 0
        for char in str:
            t = ord(char) - ord('a')
            p = j = tr[j][t]
            while p:
                ans += cnt[p]
                cnt[p] = 0
                p = fail[p]
        print(ans)

if __name__ == "__main__":
    main()
