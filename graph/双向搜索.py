from collections import deque

N = 10

def extend(q, da, db, a, b):
    t = q.popleft()
    for i in range(len(t)):
        for j in range(len(a)):
            if t[i:i+len(a[j])] == a[j]:
                state = t[:i] + b[j] + t[i+len(a[j]):]
                if state in db:
                    return da[t] + 1 + db[state]
                if state in da:
                    continue
                da[state] = da[t] + 1
                q.append(state)
    return 11

def bfs(A, B, a, b):
    qa = deque([A])
    qb = deque([B])
    da = {A: 0}
    db = {B: 0}
    while qa and qb:
        if len(qa) <= len(qb):
            t = extend(qa, da, db, a, b)
        else:
            t = extend(qb, db, da, b, a)
        if t <= 10:
            return t
    return 11

def main():
    A, B = input().split()
    if A == B:
        print("0")
        return
    n = 0
    a, b = [], []
    while True:
        try:
            x, y = input().split()
            a.append(x)
            b.append(y)
            n += 1
        except:
            break
    ans = bfs(A, B, a, b)
    if ans > 10:
        print("NO ANSWER!")
    else:
        print(ans)

if __name__ == "__main__":
    main()
